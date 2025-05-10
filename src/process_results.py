from .measure import measurements
from .problem import SSP

class process_counts:
    def __init__(self, counts:measurements,problem:SSP):
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