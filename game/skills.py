from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Skill:
    name: str
    stamina: float
    damage: float


kick = Skill(name="Свирепый пинок", damage=22, stamina=6)
thrust = Skill(name="Мощный укол", damage=15, stamina=5)
