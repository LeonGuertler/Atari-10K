import gymnasium as gym
import torch
from dataclasses import dataclass

@dataclass
class State:
    observation: torch.Tensor

def build_env():
    pass


def perform_action(action) -> State:
    pass