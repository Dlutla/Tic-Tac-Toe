"""
Интерфейс сервиса игры. Определяет методы, которые должен реализовать конкретный сервис.
Это позволяет легко подменять реализацию (например, для тестов).
"""
from abc import ABC, abstractmethod
from domain.model.game import Game

class GameService(ABC):
    @abstractmethod
    def get_computer_move(self, game: Game) -> tuple[int, int]:
        """
        Возвращает координаты (row, col) для хода компьютера.
        Если ходов нет (ничья), возвращает (-1, -1).
        """
        pass

    @abstractmethod
    def validate_move(self, game: Game, row: int, col: int, expected_player: int) -> bool:
        """
        Проверяет, может ли игрок (expected_player) сделать ход в (row, col).
        expected_player: 1 или -1.
        """
        pass

    @abstractmethod
    def is_game_over(self, game: Game) -> bool:
        """Возвращает True, если игра закончена (победа или ничья)."""
        pass