import mysql.connector
from mysql.connector import Error
from sqlalchemy import column
from sympy import Q
import pandas as pd
import numpy as np
from Bio import SeqIO
try:
    connection = mysql.connector.connect(host='132.66.207.29',
                                         database='covdb_dev_2',
                                         user='admin',
                                         password='secretpass1',
                                         port='9100')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        ## defining the Query to use
        SQL_Query = "SELECT sequence.id, sequence.sequence,sequence.sample_id,clade.clade FROM sequence INNER JOIN  clade ON sequence.id = clade.seq_id limit 10"
        cursor.execute(SQL_Query)
        data = cursor.fetchall()
        df = pd.DataFrame(data,columns=['id','sequence','sample_id','clade'])
        print(df)
        clade_df=df[['sample_id','clade']]
        list1 = clade_df.clade.unique()
        clade_df['clade'] = clade_df['clade'].astype('category').cat.codes
        Seq_df=df[['sample_id','sequence']]
        print(clade_df)
        print(Seq_df)
        Seq_df.rename(columns={'sample_id': 'id'}, inplace=True)
        vals=Seq_df.set_index('id')['sequence'].to_dict()
        """'"""""""""""""""""""""""""""""" PD--> FASTA"""""""""""""""""""""""
        ofile = open("my_fasta.txt", "w")
        for i in range(len(Seq_df)):
            ofile.write(">" + Seq_df['id'][i] + "\n" +Seq_df['sequence'][i] + "\n")
        #do not forget to close it
        ofile.close()
        clade_df.to_csv('cluster.txt', sep='\t', index=False,header=False)
        #Seq_df.to_csv('sequences.txt', index=False,header=False)
        #   print(pair)
        #print("You're connected to database: ", record)
    """'"""""""""""""""""""""""""""""" ref-seq"""""""""""""""""""""""
    
except Error as e:
    print("Error while connecting to MySQL", e)
    exit()
    
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
