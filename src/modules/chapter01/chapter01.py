"""
chapter01
"""
from __future__ import annotations

from src.modules.chapter01.Bandit import Bandit


def chapter01() -> None:
    """
    chapter01
    """
    bandit: Bandit = Bandit()

    for i in range(3):
        print(bandit.play(0))
