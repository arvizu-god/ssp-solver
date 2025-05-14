import math
from typing import List

class SSP:
    """
    Represents an SSP instance:
    A: list of integers
    t: target sum
    This class computes index and sum registers width
    """
    def ___init__(self,A:List[int],t:int):
        self.A=A
        self.t=t
        self.n_ind=len(self.A)
        self.sum_neg=sum(a for a in A if a<0)
        self.sum_pos=sum(a for a in A if a>0)
        self.range_len=self.sum_pos-self.sum_neg+1
        self.n_sum=math.ceil(math.log2(self.range_len))