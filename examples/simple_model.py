# This example comes with NeuronVisio.

# Importing the NeuronVisio
import nrnVisio

# Importing hoc interpreter
from neuron import h

# simple model
soma = h.Section()
dend1 = h.Section()
dend2 = h.Section()
soma.diam = 10
dend1.diam = 3
dend2.diam = 3  
dend1.connect(soma)
dend2.connect(soma)

# biophysics

for sec in h.allsec(): 
     sec.Ra = 100      
     sec.cm = 1         

soma.insert('hh')
dend1.insert('pas')
dend2.insert('pas')

# --------------------- Instrumentation ---------------------
# synaptic input
syn = h.AlphaSynapse(0.5, sec=soma)
syn.onset = 0.5
syn.gmax = 0.05
syn.e = 0

