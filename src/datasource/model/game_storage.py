"""
Потокобезопасное хранилище игр в памяти.
Использует threading.Lock для синхронизации доступа из разных потоков.
(В нашем случае процессы не используются, но требование есть.)
"""
from threading import Lock
from typing import Dict, Optional
import uuid

class GameStorage:
    def __init__(self):
        self._games: Dict[uuid.UUID, dict] = {}   # словарь: ID -> данные игры (словарь)
        self._lock = Lock()

    def save(self, game_id: uuid.UUID, game_data: dict):
        """Сохраняет или обновляет данные игры."""
        with self._lock:
            self._games[game_id] = game_data

    def get(self, game_id: uuid.UUID) -> Optional[dict]:
        """Возвращает данные игры или None, если не найдена."""
        with self._lock:
            return self._games.get(game_id)

    def exists(self, game_id: uuid.UUID) -> bool:
        with self._lock:
            return game_id in self._games