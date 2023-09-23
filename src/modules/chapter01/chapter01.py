"""
chapter01
"""
from __future__ import annotations

from typing import MutableSequence

import matplotlib.pyplot as plt

from src.modules.chapter01.Bandit import Bandit, Agent


def chapter01() -> None:
    """
    chapter01
    """
    steps: int = 1000
    epsilon: float = 0.1

    bandit: Bandit = Bandit()
    agent: Agent = Agent(epsilon)
    total_reward: float = 0.0
    total_rewards: MutableSequence[float] = []
    rates: MutableSequence[float] = []

    for step in range(steps):
        action: int = agent.get_action()
        reward: float = bandit.play(action)
        agent.update(action, reward)
        total_reward += reward
        total_rewards.append(total_reward)
        rates.append(total_reward / (step + 1))

    print(total_reward)
    plt.ylabel("Total reward")
    plt.xlabel("Steps")
    plt.plot(total_rewards)
    plt.show()

    plt.ylabel("Rates")
    plt.xlabel("Steps")
    plt.plot(rates)
    plt.show()
