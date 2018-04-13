"""
random_mutator.py
mutates randomly given DNA structures
> random sequences generator - 20 random DNA sequences
> models generator - from randomly mutated sequences
> calculate RMSD of models - generate tab results
"""

import sys
import os
import random


def DNAseq_retriever(i):
    """
    Retrieves the DNA sequence of the crystal structure.
    """
    DNAseq_file = DNAseqs_path + i + '_boundDNA.seq'
    seq_f = open(DNAseq_file, 'r')
    seq = seq_f.read().strip().split('\n')
    seq_one = []
    for n in seq:
        seq_one.append(n[0:1])
    return seq_one



def random_seqs_generator(n):
    """
    Retrieves an ensamble of 20 DNA random 
    sequences with DNA crystal structure length.
    """
    nts = ['A', 'T', 'C', 'G']
    d = {}
    for i in range(0,20):
        seq_name = 'seq_' + str(i)
        seq = []
        for i in range(0, n):
            nt = random.choice(nts)
            seq.append(nt)
        d[seq_name] = seq
    return d



def mutations_dict_writer(d, i):
    """
    Writes an output file with the 20 mutated sequences
    to be modeled.
    """
    out_file = out_path + str(i) + '.mseqs'
    out = open(out_file, 'w')
    for n in range(0,20):
        label = '>' + i + '_mutated_seq_' + str(n) + '\n'
        seq = str(''.join(d['seq_' + str(n)]))
        out.write(label)
        out.write(seq + '\n')
    out.close



def bound_models_generator(d, i):
    """
    Bounds the DNA models according to a specified sequence
    mainteining the crystal structure of the parental DNA molecule.
    """
    bound_path = DNAparameters_path + i + '/bound/'
    geoparams_file = bound_path + 'bp_step.par'
    geoparams_f = open(geoparams_file, 'r')
    complementary = {'A':'T', 'G':'C', 'T':'A', 'C':'G'}
    out_file_path =  out_path + i + '/bound/'

    content = geoparams_f.read()
    lines = content.strip().split('\n')
    n = len(lines) - 3
    
    for item in d:
		out_file = open(out_file_path + i + '_' + item + '_bp_step.par', 'w')
		out_file.write(str(lines[0]) + '\n')
		out_file.write(str(lines[1]) + '\n')
		out_file.write(str(lines[2]) + '\n')
	
		for m in range(0,n):
			p = m + 3
			lines[p] = list(lines[p])
			nt1 = d[item][m]
			nt2 = complementary[nt1]
			lines[p][0] = nt1
			lines[p][2] = nt2
			line = ''.join(lines[p])
			out_file.write(line + '\n')

		out_file.close()




#def unbound_models_generator():
#bound_path = DNAparameters_path + i + '/unbound/'
#def RMDS_calculator():
#def table_res_maker():

#def minimization()

path = os.getcwd()
benchmark_path = '/home/silvia/Projects-silvia/Protein-DNA_benchmark/Bonvin_BenchmarkProtDNA/Prot-DNABenchmark1.0/'
DNAseqs_path = benchmark_path + 'DNAseqs/'
DNAparameters_path = benchmark_path + 'DNAparameters/'
out_path = benchmark_path + 'MutateDNA/'

list_dirs = os.listdir(benchmark_path)
ids_list = []

for i in list_dirs:
    if len(i) == 4:
        ids_list.append(i)
#print ids_list


for i in ids_list:
    DNAseq = DNAseq_retriever(i) #list
    DNAseq_len = len(DNAseq)
    #print DNAseq, len(DNAseq)
    random_dict = random_seqs_generator(DNAseq_len)
    #print random_dict
    out_1 = mutations_dict_writer(random_dict, i)
    out_2 = bound_models_generator(random_dict, i)
    #print out_2