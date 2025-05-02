from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from .problem import SSP
from .assembly import assembly
from .grover import Grover

class sspsolver:
    def __init__(self, A, t, iterations:int):
        self.problem=SSP(A,t)
        self.iterations=iterations
        self.assembly=assembly(self.problem)
        self.grover=Grover(self.problem)

    def build(self)->QuantumCircuit:
        p=self.problem
        ind=QuantumRegister(p.n_ind,name='i')
        sum=QuantumRegister(p.n_sum,name='s')
        bit=ClassicalRegister(p.ind,name='b')
        qc=QuantumCircuit(ind,sum,bit)

        qc.h(ind)
        qc.barrier()

        for _ in range(self.iterations):
            qc.append(self.assembly.circuit(),ind[:]+sum[:])
            qc.barrier()

            qc.append(self.grover.circuit().to_gate(label='Diffusor'),ind[:])
            qc.barrier()
        
        qc.measure(ind,bit)
        return qc