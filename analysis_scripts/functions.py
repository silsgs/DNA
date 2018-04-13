#modulo funciones para pdb y mutagenesis

def parsePDBline(line):
    """
    Returns values from a PDB line
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

    vec = at_num, at_name, altern_loc, res_name, chain_id, res_num, cod_insert_res, X_coord, Y_coord, Z_coord, occup, tempfactor, element, charge

    return vec


def writePDBline(vec):
    """
    Writes a line with given values in PDB format
    in: vec of length 13.
    """

    line = "ATOM  {:5s} {:^4s}{:1s}{:3s} {:1s}{:4s}{:1s}   {:8.3f}{:8.3f}{:8.3f}{:6.2s}{:6.2s}          {:>2s}{:2s}\n".format(
        vec[0], vec[1], vec[2], vec[3], vec[4], vec[5], vec[6], float(vec[7]), float(vec[8]), float(vec[9]), (vec[10]),
        (vec[11]), vec[12], vec[13])

    return line


def pdb_fasta_downloader(out_path, list_ids):
    """
    Saves sequences in fasta format from entries of the
    Protein Data Bank.
    """
    for i in ids_list:
        url = 'https://www.rcsb.org/pdb/download/viewFastaFiles.do?structureIdList=' + i + '&compressionType=uncompressed'
        urllib.urlretrieve(url, out_path + "pdb_" + i + ".fasta")


def DNAseq_retriever(i):
    """
    Retrieves the DNA sequence from crystal structure.
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
    Builds DNA models according to a specified sequence
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