import sys
import os

# Constants

path_to_files = os.getcwd() + '/'

file1 = path_to_files + sys.argv[1]
out_file = path_to_files + sys.argv[1].replace('_ats.pdb', '_atoms.pdb')


def get_line_values(line):
    """
    Creates a vector of the values in a line
    """
    vec = line.strip().split()
        
    rec_type = vec[0]
    at_num = vec[1]
    at_name = vec[2]
    altern_loc = ' '
    res_name = 'D' + vec[3]
    chain_id = ' '
    res_num = ' '
    cod_insert_res = ' '
    X_coord = vec[4]
    Y_coord = vec[5]
    Z_coord = vec[6]
    occup = ' '
    tempfactor = ' '
    element = ' '
    charge = ' '
    
    vec = at_num, at_name, altern_loc, res_name, chain_id, res_num, cod_insert_res, X_coord, Y_coord, Z_coord, occup, tempfactor, element, charge
    
    return vec


def create_pdb_line(vec): 
    
    line = "ATOM  {:5s} {:^4s}{:1s}{:3s} {:1s}{:4s}{:1s}   {:8.3f}{:8.3f}{:8.3f}{:6.2s}{:6.2s}          {:>2s}{:2s}\n".format(vec[0], vec[1], vec[2], vec[3], vec[4], vec[5], vec[6], float(vec[7]), float(vec[8]), float(vec[9]), (vec[10]), (vec[11]), vec[12], vec[13])
    
    return line



if __name__ == "__main__":
    
    f1 = open(file1, 'r')
    outf = open(out_file, 'w')
    
    for line in f1:
        vec_line = get_line_values(line)
        
        #vec_line = line.strip().split()
        #print vec_line
        
        pdb_line = create_pdb_line(vec_line)
        outf.write(pdb_line)
        
    f1.close()
    outf.close()
