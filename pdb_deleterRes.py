#author: Silvia M. Gimenez

import sys
from Bio.PDB import *


class ResSelect(Select):
    def accept_residue(self, residue):
        if residue.id[1] >= start_res and residue.id[1] <= end_res:
            return False
        else:
            return True



if __name__ == "__main__":
    pdbfile = sys.argv[1]

    parser=PDBParser()

    structure = parser.get_structure('dna', pdbfile) # load your molecule

    start_res = float(sys.argv[2])
    end_res = float(sys.argv[3])

    io=PDBIO()
    io.set_structure(structure)
    io.save(sys.argv[1].replace(".pdb", "_cropped.pdb"), select=ResSelect())

