#with open('sequence.txt') as f:
#    lines = f.readlines()
#print(lines)

#cwd = os.getcwd()

# Print the current working directory
#print("Current working directory: {0}".format(cwd))


import os
#os.system("python run.py --input  c:/Users/shade/Desktop/עבודות/ShomronLab/Mybolotie/sequnecs.txt --reference c:/Users/shade/Desktop/עבודות/ShomronLab/Mybolotie/sequence.txt --outdir c:/Users/shade/Desktop/עבודות/ShomronLab/bolotie --cluster c:/Users/shade/Desktop/עבודות/ShomronLab/Mybolotie/clade.txt")
os.system("python run.py --input c:/Users/shade/Desktop/עבודות/ShomronLab/Mybolotie/my_fasta.txt --reference c:/Users/shade/Desktop/עבודות/ShomronLab/Mybolotie/ref_seq.fasta --outdir c:/Users/shade/Desktop/עבודות/ShomronLab/Mybolotie --clusters c:/Users/shade/Desktop/עבודות/ShomronLab/Mybolotie/cluster.txt")

#import run
#run.main(['--input', 'c:/Users/shade/Desktop/עבודות/ShomronLab/Mybolotie/sequnecs.txt','--reference','c:/Users/shade/Desktop/עבודות/ShomronLab/Mybolotie/sequence.txt','--outdir','c:/Users/shade/Desktop/עבודות/ShomronLab/bolotie'])