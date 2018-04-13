"""
imports fasta files from pdb
"""

import urllib
import os

path = os.getcwd().replace('Fasta-files', '')
ids_list = os.listdir(path)

for i in ids_list:
    url = 'https://www.rcsb.org/pdb/download/viewFastaFiles.do?structureIdList=' + i + '&compressionType=uncompressed'
    urllib.urlretrieve(url, "pdb_" + i + ".fasta")

