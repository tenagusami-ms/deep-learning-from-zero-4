"""
bandit problem
"""
from __future__ import annotations

import numpy as np


class Bandit:
    """
    bandit problem
    """

    def __init__(self, arms: int = 10):
        self.rates: np.ndarray = np.random.rand(arms)

    def play(self, arm: int) -> float:
        """
        play
        """
        rate: float = self.rates[arm]
        return 1.0 if rate > np.random.rand() else 0.0
