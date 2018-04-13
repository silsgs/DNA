import sys
import os
import matplotlib
#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""
python histpoloter.py 
"""

# constants
#rep_no = 'rep-' + sys.argv[1]

ene_file = sys.argv[1]
path = os.getcwd() + '/'

dnt = ['A', 'T', 'G', 'C']

fig = plt.figure(figsize=(15,10))
st = fig.suptitle("XXX", x = 0.5, y = 1.03, fontsize = 17)

n_bins = 100
c = 0

for i in dnt:
    
    #data_file = np.loadtxt(fname = path + rep_no + '/' + 'rep-' + i +'/3mfk.ene', skiprows = 2, usecols=[1,2,3,4,5])
    data_file = np.loadtxt(fname = path + sys.argv[1], skiprows = 2, usecols=[1,2,3,4,5])
    ele = data_file[ : ,0]
    desolv = data_file[ : ,1]
    VdW = data_file[ : ,2]
    total_E = data_file[ : ,3]
    
    energetic_terms = [total_E, ele, desolv, VdW]
    
    for a in energetic_terms:
    
        c = c + 1
        ax = plt.subplot(4,4,c)
        n, bins, patches = ax.hist(a, n_bins, normed=1)
        avg = np.mean(a)
        var = np.var(a)
        pdf_x = np.linspace(np.min(a),np.max(a),100)
        pdf_y = 1.0/np.sqrt(2*np.pi*var)*np.exp(-0.5*(pdf_x-avg)**2/var)
        
        """
        while n == [1 , 5, 9 ,13]:
            ax.set_ylabel('Probability density')
        
        while n == 1:
            ax.set_title('pyDock score')
        
        while n == 2:
            ax.set_title('Electrostatics')
        
        while n == 3:
            ax.set_title('Desolvation')
        
        while n == 4:
            ax.set_title('Van der Waals')
        """        
        
        ax.plot(pdf_x,pdf_y)


plt.tight_layout()
plt.savefig(path + '/multiplot_' + sys.argv[1].replace('.ene','') +'.png', dpi=350)
plt.show()

