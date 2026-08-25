"""
Модели для передачи данных по HTTP (DTO).
Используем dataclass для удобства.
"""
from dataclasses import dataclass
from typing import List

@dataclass
class GameWeb:
    id: str
    field: List[List[int]]