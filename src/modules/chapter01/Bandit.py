"""
bandit problem
"""
from __future__ import annotations

from typing import cast

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
        rate: np.float64 = cast(np.float64, self.rates[arm])
        return 1.0 if rate > np.random.rand() else 0.0


class Agent:
    def __init__(self, epsilon: float, action_size: int = 10):
        self.epsilon: float = epsilon
        self.Qs: np.ndarray = np.zeros(action_size)
        self.ns: np.ndarray = np.zeros(action_size)

    def update(self, action: int, reward: float) -> None:
        self.ns[action] += 1
        self.Qs[action] += (reward - self.Qs[action]) / self.ns[action]

    def get_action(self) -> int:
        if np.random.rand() < self.epsilon:
            return np.random.randint(0, len(self.Qs))
        return np.argmax(self.Qs)
