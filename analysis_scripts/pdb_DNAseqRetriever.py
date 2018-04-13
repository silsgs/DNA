"""
Retrieves DNA fasta seq from others fasta files
"""
import os
from Bio import SeqIO

path = os.getcwd() + '/'
print path
nt_list = ['A', 'T', 'G', 'C']

for i in os.listdir(path):
    if '.fasta' in i:
        out_f = open(path + i.replace('.fasta', '_DNA.fasta'), 'w')
        for seq_record in SeqIO.parse(i, "fasta"):
            #print(seq_record.id)
            #print(seq_record.seq)
            As = seq_record.seq.count('A')
            Ts = seq_record.seq.count('T')
            Gs = seq_record.seq.count('G')
            Cs = seq_record.seq.count('C')
            num = As + Ts + Gs + Cs
            if num == len(seq_record.seq):
                print 'This is DNA'
                out_f.write('>' + seq_record.id + '\n')
                out_f.write(str(seq_record.seq) + '\n')
        out_f.close()