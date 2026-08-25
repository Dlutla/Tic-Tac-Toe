"""
Контейнер зависимостей. Создаёт и предоставляет экземпляры классов.
Реализует паттерн Singleton для хранилища.
"""
from datasource.model.game_storage import GameStorage
from datasource.repository.game_repository import GameRepository
from domain.service.minimax_service import MinimaxGameService

class Container:
    def __init__(self):
        self._storage = None
        self._repository = None
        self._game_service = None

    @property
    def storage(self) -> GameStorage:
        """Singleton хранилище."""
        if self._storage is None:
            self._storage = GameStorage()
        return self._storage

    @property
    def repository(self) -> GameRepository:
        if self._repository is None:
            self._repository = GameRepository(self.storage)
        return self._repository

    @property
    def game_service(self) -> MinimaxGameService:
        if self._game_service is None:
            self._game_service = MinimaxGameService(computer_symbol=1, human_symbol=-1)
        return self._game_service