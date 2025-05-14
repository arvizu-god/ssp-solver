from qiskit import transpile
from qiskit_aer import AerSimulator, QasmSimulator

class Measurements:
    def __init__(self, qc:QuantumCircuit,shots:int):
        self.qc=qc
        self.simulator=AerSimulator()
        self.shots=shots

    def measure(self)-> Dict[str, int]:
        tqc=transpile(qc, self.simulator)
        result=self.simulator.run(tqc,shots=self.shots).result()
        counts=result.get_counts()

        return counts
