"""
ssp_solver: A Qiskit-based Subset-Sum Problem solver library.

Exposes:
  - SSPProblem       : Defines the problem instance and parameters.
  - SumGate, SubGate : Arithmetic gates for adding/subtracting Aᵢ.
  - PhaseOracle      : Phase oracle for target-sum testing.
  - SSPAssembler     : Builds the sum–oracle–subtract step.
  - SSPSolver        : Full Grover-based SSP solver.
  - MeasurementsProcessor : Helpers to turn raw counts into solutions.
"""

__version__ = "0.1.0"

from .problem import SSP
from .gates import SumGate, SubGate
from .oracle import oracle
from .assembly import assembly
from .solver import sspsolver
from .measure import measurements

__all__ = [
    "SSP",
    "SumGate", "SubGate",
    "oracle",
    "assembly",
    "sspsolver",
    "measurements",
]