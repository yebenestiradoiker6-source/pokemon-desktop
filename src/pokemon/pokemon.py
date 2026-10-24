from dataclasses import dataclass


@dataclass
class Pokemon:
    species: str
    name: str
    x: float = 200.0
    y: float = 200.0
    width: int = 96
    height: int = 96
    speed: float = 120.0
    direction: int = 1
    hunger: float = 75.0
    happiness: float = 80.0
    energy: float = 70.0
    health: float = 100.0
    state: str = "IDLE"
