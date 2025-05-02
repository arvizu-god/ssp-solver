from qiskit import QuantumRegister, QuantumCircuit
from qiskit.circuit.library import QFT
from .problem import SSP
from .gates import SumGate,SubGate
from .oracle import Oracle

class assembly:
    def __init__(self,problem:SSP):
        self.problem=problem
        self.sum_gate=SumGate(problem).to_gate()
        self.sub_gate=SubGate(problem).to_gate()
        self.oracle=Oracle(problem).to_gate()
        self.qft=QFT(problem.n_sum,do_swaps=False).to_gate()
        self.iqft=QFT(problem.n_sum,do_swaps=False).to_gate()

    def circuit(self)->QuantumCircuit:
        ind=QuantumRegister(self.problem.n_ind,name='i')
        sum=QuantumRegister(self.problem.n_sum,name='s')
        qc=QuantumCircuit(ind,sum,name='assembly')

        qc.append(self.qft,sum)
        qc.append(self.sum_gate,ind[:]+sum[:])
        qc.append(self.iqft,sum)

        qc.append(self.oracle,sum[:])

        qc.append(self.qft,sum)
        qc.append(self.sub_gate,ind[:]+sum[:])
        qc.append(self.iqft,sum)

        return qc