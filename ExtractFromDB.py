import mysql.connector
from mysql.connector import Error
from sqlalchemy import column
from sympy import Q
import pandas as pd
import numpy as np
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
        SQL_Query = "SELECT sequence.id, sequence.sequence,clade.clade FROM sequence INNER JOIN  clade ON sequence.id = clade.seq_id limit 10"
        cursor.execute(SQL_Query)
        data = cursor.fetchall()
        df = pd.DataFrame(data,columns=['id','sequence','clade'])
        print(df)
        clade_df=df[['sequence','clade']]
        Seq_df=df['sequence']
        print(clade_df)
        print(Seq_df)
        clade_df.to_csv('clade.txt', sep='\t', index=False,header=False)
        Seq_df.to_csv('sequence.txt', index=False,header=False)
        #   print(pair)
        #print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
    exit()
    
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
