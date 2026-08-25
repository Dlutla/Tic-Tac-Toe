"""
Репозиторий для работы с хранилищем игр.
Скрывает детали хранения (в памяти) и предоставляет методы save/get.
"""
from datasource.model.game_storage import GameStorage
from datasource.mapper import game_mapper
from domain.model.game import Game

class GameRepository:
    def __init__(self, storage: GameStorage):
        self.storage = storage

    def save(self, game: Game):
        """Сохраняет игру в хранилище."""
        data = game_mapper.from_domain(game)
        self.storage.save(game.id, data)

    def get(self, game_id) -> Game:
        """Загружает игру из хранилища. Если не найдена, бросает исключение."""
        data = self.storage.get(game_id)
        if data is None:
            raise ValueError("Game not found")
        return game_mapper.to_domain(data)

    def exists(self, game_id) -> bool:
        return self.storage.exists(game_id)