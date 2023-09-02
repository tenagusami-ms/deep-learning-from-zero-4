"""
bandit problem
"""
from __future__ import annotations

import numpy as np
from numpy.typing import NDArray


class Bandit:
    """
    bandit problem
    """

    def __init__(self, arms: int = 10):
        self.rates: NDArray[np.float64] = np.random.rand(arms)

    def play(self, arm: int) -> float:
        """
        play
        """
        rate: np.float64 = self.rates[arm]
        print(np.isscalar(rate))
        return 1.0 if rate > np.random.rand() else 0.0

    def a(self):
        """
        a
        """
        b: NDArray[np.int32] = np.array([1, 2, 3])
        b0: np.int32 = b[0]
