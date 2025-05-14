from .Measure import Measurements
from .Problem import SSP
from .Assembly import Assembly

class ProcessCounts:
    def __init__(self, counts:Measurements,problem:SSP):
        self.counts=counts
        self.values=problem.A
        self.target_sum=problem.t

    def process_counts(self,counts, values,target_sum):
        total_measurements=sum(list(counts.values))
        counts=dict(sorted(counts.items(), key=lambda state:state[1],reverse=True))
        counts=list(counts.items())

        answer_subsets=[]
        for state, count in counts:
            subset_qubits=list(reversed(state[1:]))

            subset=[]
            for index, value in enumerate(subset_qubits):
                if value=='1':
                    subset.append(self.values[index])
            
            if sum(subset)==self.target_sum:
                answer_subsets.append((subset,count/total_measurements))
            else:
                break

        return answer_subsets
    
    def circuit_stats(self,circuit:Assembly):
        self.circuit=Assembly.circuit
        cs_dict={'num_qubits':self.circuit.num_qubits,'num_clbits':self.circuit.num_clbits,'depth':self.circuit.depth(),'size':self.circuit.size(),'count_ops':self.circuit.count_ops()}
        return cs_dict