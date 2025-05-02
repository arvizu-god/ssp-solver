from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit import Gate
from .problem import SSP

class Grover:
    def __init__(self,problem:SSP):
        self.n_ind=problem.n_ind
    
    def grover(self)->Gate:
        ind=QuantumRegister(self.n_ind,name='i')
        qc=QuantumCircuit(ind,name='diffusor')

        for j in range(self.n_ind):
            qc.h(j)
            qc.x(j)

        qc.h(ind[-1])
        qc.mcx(ind[:-1],ind[-1],mode='noancilla')
        qc.h(ind[-1])

        for j in range(self.n_ind):
            qc.x(j)
            qc.h(j)

        return qc.to_gate(label='diffusor')