import sys
import os
import numpy as np

"""
Usage : python l-geompoint.py <id_case> <n-poses>
"""

# Constants

path = os.getcwd() + '/'
id_case = sys.argv[1]
ini_file = path + id_case + '.ini'


def define_chains(f):
    """
    Define lig_chains to calculate its lgp from an ensemble of poses
    """
    f = open(f, 'r')
    for i,line in enumerate(f):
        
        if i == 8:
            vec = line.strip().split('=')
            
            if ',' in vec[1]:
                names = vec[1].split(',')
                return names
            
            else:
                name = vec[1]
                return name
    f.close()


def calculate_mean_coord(f):
    """
    Creates a vector of means of x, y, z coordinates from a model pose (pdb)
    """
    pdb_file = open(f, 'r')
    vec_x = []
    vec_y = []
    vec_z = []

    for line in pdb_file:
        rec_type = line[0:6]
        at_no = line[6:11]
        at_na = line[12:16]
        res_na = line[17:20]
        chain_id = line[21]
        res_no = line[22:26]
        X_coord = line[30:38]
        Y_coord = line[38:46]
        Z_coord = line[46:54]
        occup = line[54:60]
        tempfactor = line[60:66]
        element = line[76:78]
        charge = line[78:80]
        if chain_id in lig_chains:
            vec_x.append(float(X_coord.strip(' ')))
            vec_y.append(float(Y_coord.strip(' ')))
            vec_z.append(float(Z_coord.strip(' ')))

    pdb_file.close()
    return np.mean(vec_x), np.mean(vec_y), np.mean(vec_z)



def create_pdb_from_points(index, point):
    """
    Creates a PDB ATOM format line which contains an atom_type atom for each mean vector coordinates.
    """
    atom_type = 'H'
    line = "ATOM  %5d %-4s XXX    1     %8.3f%8.3f%8.3f\n" % (index, atom_type,
                                                                  point[0], point[1], point[2])
    return line



if __name__ == "__main__":
    """
    Creates a model with each geometric central point
    for each model pose.
    """

    lig_chains = define_chains(ini_file)
    print lig_chains
    
    n_poses = '1 ' + sys.argv[2]
    command = 'pydock3 ' + id_case + ' makePDB ' + n_poses + ' ' + id_case + '.ene lg-'
    os.system(command)

    out_f = open(id_case + '_lgp_top' + sys.argv[2] + '.pdb', 'w')

    allfiles = os.listdir(path)
    index = 0
    
    for i in allfiles:
        if 'lg-' in i:
            mean_vec = calculate_mean_coord(i)         
            
            index = index + 1
            atom_line = create_pdb_from_points(index, mean_vec)
            out_f.write(atom_line)


    out_f.close()
    os.system('rm lg-*')

