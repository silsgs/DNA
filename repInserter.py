import sys

"""
Usage : python repInserter.py <chain_model> <start_no_res> <end_no_res> <nt_to_insert>

ej : python repInserter.py 3mfk_C.pdb 4 7 A
"""

def parse_pdb_line(line, res_list, res_na):
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
    X_coord = line[30:38]
    Y_coord = line[38:46]
    Z_coord = line[46:54]
    occup = line[54:60]
    tempfactor = line[60:66]
    element = line[76:78]
    charge = line[78:80]
    
    if res_num in res_list:
        res_name == str(res_na)
        vec = at_num, at_name, altern_loc, res_name, chain_id, res_num, cod_insert_res, X_coord, Y_coord, Z_coord, occup, tempfactor, element, charge
    
    else:
        vec = at_num, at_name, altern_loc, res_name, chain_id, res_num, cod_insert_res, X_coord, Y_coord, Z_coord, occup, tempfactor, element, charge
        
    return vec




def create_atoms_list(f):
    
    atoms_file = open(f, 'r')
    atoms_list = []
    
    for i in atoms_file:
        ii = i.strip()
        atoms_list.append(ii)
    
    atoms_file.close()
    return atoms_list



def select_atoms(atoms_list, vec, res_na):
    """
    Retrieves a list of the atoms of the nts
    """
    
    vec = list(vec)
    
    atom = str(vec[1].strip(' '))
    
    if atom in atoms_list:
        vec[3] = ' ' + res_na
        return vec
    
    else:
        return 'empty'
    



def create_pdb_line(vec):
    """
    Creates a PDB format line from a vector of values
    """
    #line = "ATOM  %5d %-4s XXX    1     %8.3f%8.3f%8.3f\n" % (index, atom_type, point[0], point[1], point[2])
    #ATOM      4  O4'  DG C   1      61.436  59.276  36.865  1.00 54.81           O
    
    line = "ATOM  {:5s} {:^4s}{:1s}{:3s} {:1s}{:4s}{:1s}   {:8.3f}{:8.3f}{:8.3f}{:6.2f}{:6.2f}          {:>2s}{:2s}\n".format(vec[0], vec[1], vec[2], vec[3], vec[4], vec[5], vec[6], float(vec[7]), float(vec[8]), float(vec[9]), float(vec[10]), float(vec[11]), vec[12], vec[13])
    return line





# Constants
path = '/home/silvia/Project/Mutagenesis/3mfk/Repeats/complex_pdbs/'
f1 = path + sys.argv[1]

start_no_res = int(sys.argv[2])
end_no_res = int(sys.argv[3])
res_na = 'D' + sys.argv[4]
res_list = str(range(start_no_res, end_no_res + int(1)))

f2 = '/home/silvia/Project/Mutagenesis/3mfk/Repeats/' + res_na + '_ats.txt'



if __name__ == "__main__":
    """
    
    """
    pdb_file = open(f1, 'r')
    
    atoms_list = create_atoms_list(f2)
        
    out_f = open(sys.argv[1].replace('.pdb', '_' + res_na + '.pdb'), 'w')
    
        
    for line in pdb_file:
        vec_line = parse_pdb_line(line, res_list, res_na)
        
        res_no = str(vec_line[5].strip(' '))
                
        if res_no in res_list:
            vec_line = select_atoms(atoms_list, vec_line, res_na)
            
            if vec_line != 'empty':
                pdb_line = create_pdb_line(vec_line)
                out_f.write(pdb_line)
                
            else:
                continue
        
        else:
            pdb_line = create_pdb_line(vec_line)
            out_f.write(pdb_line)
    
    
    pdb_file.close()
    out_f.close()
