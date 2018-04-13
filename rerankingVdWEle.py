import sys
import os
import pandas as pd
from pandas import *
import numpy as np
from libpydock.util.Table import Table

"""
usage: python rerankingVdWEle.py <id_case>
"""

path = os.getcwd() + '/'
id_case = sys.argv[1]
ene_file = path + id_case + '.ene'
ene_file_clean = path + id_case + '_clean.ene'
ene_file_clean_PVdW = path + id_case + '_clean_vdw.ene'


def clean_ene_file(f):
    """
    Removes headers
    """
    command1 = 'tail -n +3 ' + ene_file + '>' + ene_file_clean
    os.system(command1)

    
def remove_posistive_VDW(f):
    """
    Removes poses with positive VdW energies
    """
    command2 = "awk '{for (i=0;i<=NF;i++) {if ($4>0) next}; if ($4<0) print}' " + ene_file_clean + ">" + ene_file_clean_PVdW
    os.system(command2)





if __name__ == "__main__":
    
    command1 = 'tail -n +3 ' + ene_file + '>' + ene_file_clean
    os.system(command1)
    
    command2 = "awk '{for (i=0;i<=NF;i++) {if ($4>0) next}; if ($4<0) print}' " + ene_file_clean + ">" + ene_file_clean_PVdW
    os.system(command2)
    
    ene_f = open(ene_file_clean_PVdW, 'r').readlines()
    
    out1 = open(path + 'out1.txt', 'w')
    
    
    #numpy and pandas method
    data_file = np.loadtxt(fname = ene_file_clean_PVdW, usecols=[0,1,2,3,4,5])
    
    df = pd.DataFrame(data_file, columns = ['Conf', 'ele', 'Desolv', 'VdW','Total' ,'Rank'])
    df['eleVdW'] = df['ele'] + df['VdW']
    
    result = df.sort_values(['eleVdW'])
    result['Rank2'] = result['eleVdW'].rank(ascending=1)
    
    
    #np.savetxt(out1, result.values, fmt='%0:d,%10.3f', delimiter="\t", header="Conf\tEle\tDesolv\tVdW\tTotal\tRANK\teleVdW\tRank2\n")
    
    
    enetab = Table([result['Conf'],result['ele'],result['eleVdW'],result['VdW']],["Conf","Ele","eleVdW","VDW"])
    
    
    #enetab.sort("eleVdW")
    #enetab.add_index_column()
    #os.system("")
    enetab.write(out1)
    #log.info("Done.")

    #print enetab
