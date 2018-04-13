import sys

"""
Usage : python removerCoord.py <chain_model> <start_no_res> <end_no_res> <nt_to_insert>

ej : python repInserter.py 3mfk_C.pdb 4 7 A
"""

def parse_pdb_line(line):
    """
    Rename residues
    """
    rec_type = line[0:6]
    at_num = line[6:11]
    at_name = line[12:16]
    altern_loc = line[16:17]
    res_name = line[17:20]
    chain_id = line[21]
    res_num = line[22:26]
    cod_insert_res = line[26:27]
    X_coord = '0.0'
    Y_coord = '0.0'
    Z_coord = '0.0'
    occup = line[54:60]
    tempfactor = line[60:66]
    element = line[76:78]
    charge = line[78:80]
    
    vec = at_num, at_name, altern_loc, res_name, chain_id, res_num, cod_insert_res, X_coord, Y_coord, Z_coord, occup, tempfactor, element, charge
        
    return vec


def create_pdb_line(vec):
    """
    Creates a PDB format line from a vector of values
    """
    #line = "ATOM  %5d %-4s XXX    1     %8.3f%8.3f%8.3f\n" % (index, atom_type, point[0], point[1], point[2])
    #ATOM      4  O4'  DG C   1      61.436  59.276  36.865  1.00 54.81           O
    
    line = "ATOM  {:5s} {:^4s}{:1s}{:3s} {:1s}{:4s}{:1s}   {:8.3f}{:8.3f}{:8.3f}{:6.2f}{:6.2f}          {:>2s}{:2s}\n".format(vec[0], vec[1], vec[2], vec[3], vec[4], vec[5], vec[6], float(vec[7]), float(vec[8]), float(vec[9]), float(vec[10]), float(vec[11]), vec[12], vec[13])
    return line





# Constants
path = '/home/silvia/Project/Mutagenesis/3mfk/Instertions/ins-1/test-case-1/'

f1 = path + sys.argv[1]


if __name__ == "__main__":
    """
    
    """
    pdb_file = open(f1, 'r')
    
    out_f = open(sys.argv[1].replace('.pdb', 'nocoords.pdb'), 'w')
    
        
    for line in pdb_file:
        vec_line = parse_pdb_line(line)
        
        pdb_line = create_pdb_line(vec_line)
        
        out_f.write(pdb_line)
    
    
    pdb_file.close()
    out_f.close()
