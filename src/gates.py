import numpy as np
from qiskit import QuantumRegister, QuantumCircuit  
from qiskit.circuit import Gate
from .problem import SSP

class SumGate:
    """
    Controlled Draper adder gate: adds A_i into the sum register
    """
    def __init__(self,problem:SSP):
        self.A=problem.A
        self.n_ind=problem.n_ind
        self.n_sum=problem.n_sum

    def to_gate(self)-> Gate:
        ind=QuantumRegister(self.n_ind,name='i')
        reg=QuantumRegister(self.n_sum,name='s')
        qc=QuantumCircuit(ind,reg,name='Sum')
        mod=2**self.n_sum

        for k,a in enumerate(self.A):
            a_mod=a%mod
            for j in range(self.n_sum):
                phi=(2*np.pi*a_mod)/(2**(j+1))
                qc.cp(phi,ind[k],reg[j])
        return qc.to_gate()
class SubGate:
    """
    Controlled Draper substraction gate: substracts A_i into the sum register
    """
    def __init__(self,problem:SSP):
        self.A=problem.A
        self.n_ind=problem.n_ind
        self.n_sum=problem.n_sum

    def to_gate(self)-> Gate:
        ind=QuantumRegister(self.n_ind,name='i')
        sum=QuantumRegister(self.n_sum,name='s')
        qc=QuantumCircuit(ind,sum,name='Sub')
        mod=2**self.n_sum

        for k,a in enumerate(self.A):
            neg=(-a)%mod
            for j in range(self.n_sum):
                phi=(2*np.pi*neg)/(2**(j+1))
                qc.cp(phi,ind[k],sum[j])
        return qc.to_gate()
