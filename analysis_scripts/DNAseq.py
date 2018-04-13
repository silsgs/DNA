"""
Downloader of DNA sequences from protein-DNA complexes
"""

import sys
import os
from Bio.PDB import *

path = os.getcwd() + '/'
DNA_files = path.replace('DNAseqs/', '')
id_list = os.listdir(DNA_files)
parser = PDBParser()

def parseResline(line):
    values = line.split()
    nt = values[1]
    return nt


for i in id_list:
    if len(i) > 4:
        continue
    else:
        b_structure = parser.get_structure(i + 'b_DNA', DNA_files + i + '/' + i + '_bound-DNA.pdb')
        out_b_structure = open(path + i + '_boundDNA.seq', 'w')
        for model in b_structure:
            for chain in model:
                for res in chain:
                    nt = parseResline(str(res))
                    #print nt
                    out_b_structure.write(nt + '\n')
                    
        
        unb_structure = parser.get_structure(i + 'unb_DNA', DNA_files + i + '/DNA_unbound.pdb')
        out_unb_structure = open(path + i + '_unboundDNA.seq', 'w')
        for model in unb_structure:
            for chain in model:
                for res in chain:
                    #print res
                    nt = parseResline(str(res))
                    #print nt
                    out_unb_structure.write(nt + '\n')