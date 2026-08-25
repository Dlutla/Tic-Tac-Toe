"""
Реализация сервиса игры с использованием алгоритма Минимакс.
Компьютер играет оптимально.
"""
from domain.model.game import Game, GameField
from domain.service.game_service import GameService

class MinimaxGameService(GameService):
    def __init__(self, computer_symbol: int = 1, human_symbol: int = -1):
        self.computer = computer_symbol   # чем ходит компьютер (1)
        self.human = human_symbol         # чем ходит человек (-1)

    def get_computer_move(self, game: Game) -> tuple[int, int]:
        """Вычисляет лучший ход для компьютера, используя минимакс."""
        best_score = -float('inf')
        best_move = None
        # Перебираем все пустые клетки
        for i in range(3):
            for j in range(3):
                if game.field.get_cell(i, j) == 0:
                    # Пробуем поставить компьютера
                    game.field.set_cell(i, j, self.computer)
                    score = self._minimax(game.field, 0, False)
                    game.field.set_cell(i, j, 0)  # откатываем ход
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        if best_move is None:
            return (-1, -1)   # нет свободных клеток
        return best_move

    def _minimax(self, field: GameField, depth: int, is_maximizing: bool) -> int:
        """
        Рекурсивный алгоритм минимакс.
        depth - глубина рекурсии (используется для предпочтения более быстрых побед)
        is_maximizing: True - ход компьютера (максимизируем), False - ход человека (минимизируем)
        """
        winner = self._check_winner(field)
        if winner == self.computer:
            return 10 - depth   # победа компьютера
        if winner == self.human:
            return depth - 10   # победа человека
        if field.is_full():
            return 0            # ничья

        if is_maximizing:
            best = -float('inf')
            for i in range(3):
                for j in range(3):
                    if field.get_cell(i, j) == 0:
                        field.set_cell(i, j, self.computer)
                        best = max(best, self._minimax(field, depth + 1, False))
                        field.set_cell(i, j, 0)
            return best
        else:
            best = float('inf')
            for i in range(3):
                for j in range(3):
                    if field.get_cell(i, j) == 0:
                        field.set_cell(i, j, self.human)
                        best = min(best, self._minimax(field, depth + 1, True))
                        field.set_cell(i, j, 0)
            return best

    def _check_winner(self, field: GameField) -> int:
        """Проверяет, есть ли победитель. Возвращает 1, -1 или 0."""
        lines = []
        for i in range(3):
            lines.append([field.get_cell(i, j) for j in range(3)])
            lines.append([field.get_cell(j, i) for j in range(3)])
        lines.append([field.get_cell(i, i) for i in range(3)])
        lines.append([field.get_cell(i, 2 - i) for i in range(3)])

        for line in lines:
            if all(cell == self.computer for cell in line):
                return self.computer
            if all(cell == self.human for cell in line):
                return self.human
        return 0

    def validate_move(self, game: Game, row: int, col: int, expected_player: int) -> bool:
        """
        Проверяет, что ход допустим: клетка существует, пуста, и ожидаемый игрок не 0.
        """
        if expected_player == 0:
            return False
        if not (0 <= row < 3 and 0 <= col < 3):
            return False
        return game.field.get_cell(row, col) == 0

    def is_game_over(self, game: Game) -> bool:
        """Игра окончена, если есть победитель или поле заполнено."""
        return self._check_winner(game.field) != 0 or game.field.is_full()