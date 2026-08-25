"""
Маппер для преобразования между domain-объектами и словарями для хранения.
"""
import uuid
from domain.model.game import Game, GameField

def to_domain(data: dict) -> Game:
    """Преобразует словарь (из хранилища) в объект Game."""
    game_id = uuid.UUID(data['id'])
    field_data = data['field']
    field = GameField()
    field.matrix = field_data
    return Game(game_id, field)

def from_domain(game: Game) -> dict:
    """Преобразует объект Game в словарь для хранения."""
    return {
        'id': str(game.id),
        'field': game.field.to_list()
    }