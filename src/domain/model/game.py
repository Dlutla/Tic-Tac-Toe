"""
Модели игрового поля и игры для domain-слоя.
Содержит только бизнес-логику, не зависит от внешних слоёв.
"""
import uuid
from typing import List

class GameField:
    """
    Игровое поле 3x3.
    Значения: 0 - пусто, 1 - крестик (компьютер), -1 - нолик (игрок).
    """
    def __init__(self, size: int = 3):
        self.size = size
        self.matrix = [[0 for _ in range(size)] for _ in range(size)]

    def set_cell(self, row: int, col: int, value: int):
        """Устанавливает значение в указанной ячейке."""
        self.matrix[row][col] = value

    def get_cell(self, row: int, col: int) -> int:
        """Возвращает значение ячейки."""
        return self.matrix[row][col]

    def to_list(self) -> List[List[int]]:
        """Возвращает поле в виде списка списков (для JSON)."""
        return self.matrix

    def is_full(self) -> bool:
        """Проверяет, заполнено ли поле целиком (ничья)."""
        return all(cell != 0 for row in self.matrix for cell in row)

    def clone(self):
        """Создаёт глубокую копию поля (нужно для алгоритма минимакс)."""
        new_field = GameField(self.size)
        new_field.matrix = [row[:] for row in self.matrix]
        return new_field

class Game:
    """
    Представляет собой одну игру: уникальный идентификатор и текущее состояние поля.
    """
    def __init__(self, game_id: uuid.UUID = None, field: GameField = None):
        self.id = game_id or uuid.uuid4()
        self.field = field or GameField()