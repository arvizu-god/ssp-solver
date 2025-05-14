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

from .Problem import SSP
from .Gates import SumGate, SubGate
from .Oracle import oracle
from .Assembly import assembly
from .Solver import sspsolver
from .Measure import measurements

__all__ = [
    "SSP",
    "SumGate", "SubGate",
    "Oracle",
    "Assembly",
    "sspsolver",
    "measurements",
]