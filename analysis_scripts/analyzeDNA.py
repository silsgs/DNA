import sys
import os

#def
path = '/home/silvia/Projects-silvia/Protein-DNA_benchmark/Prot-DNABenchmark/'
out_path = path + 'DNAparameters/'

dirs_list = os.listdir(path)
print dirs_list

for i in dirs_list:
    if len(i) > 4:
        continue
    else:
        #os.system('mkdir ' + i)
        #os.system('mkdir ' + out_path + i + '/unbound')
        #os.system('mkdir ' + out_path + i + '/bound')
        unbound_path = out_path + i + '/unbound/'
        bound_path = out_path + i + '/bound/'

        file_b_name = i + '_bound-DNA.pdb'
        file_unb_name = 'DNA_unbound.pdb'
        
        os.chdir(unbound_path)
        os.system('find_pair ' + path + i + '/' + file_unb_name + ' ' + file_unb_name.replace('.pdb', '.bps'))
        os.system('analyze ' + file_unb_name.replace('.pdb', '.bps'))
            
        os.chdir(bound_path)
        os.system('find_pair ' + path + i + '/' + file_b_name + ' ' + file_b_name.replace('.pdb', '.bps'))
        os.system('analyze ' + file_b_name.replace('.pdb', '.bps'))


#find_pair <in>.pdb <out>.bps
#analyze <out>.bps