from qiskit import QuantumRegister, QuantumCircuit
from qiskit.circuit import Gate
from .problem import SSP

class Oracle:
    """
    Class that implements a X-H-MCX-H-X phase oracle on the sum register
    """

    def __init__(self,problem:SSP):
        self.t=problem.t
        self.n_sum=problem.n_sum

    def to_gate(self)->Gate:
        sum=QuantumRegister(self.n_sum,name='s')
        qc=QuantumCircuit(sum,name='Oracle')

        for j in range(self.n_sum):
            if ((self.t>>j)&1)==0:
                qc.x(sum[j])
        
        qc.h(sum[-1])
        qc.mcx(sum[:-1],sum[-1],mode='noancilla')
        qc.h(sum[-1])

        for j in range(self.n_sum):
            if ((self.t>>j)&1)==0:
                qc.x(sum[j])

        return qc.to_gate(name='Oracle')