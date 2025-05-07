from qiskit import transpile
from qiskit_aer import AerSimulator, QasmSimulator

class measurements:
    def __init__(self, shots:int):
        self.simulator=AerSimulator()
        self.shots=shots

    def measure(self,circuit):
        tqc=transpile(circuit, self.simulator)
        result=self.simulator.run(tqc).result()
        counts=result.get_counts()

        return counts

