"""
Маппер между domain-объектами и web-моделями.
"""
import uuid
from domain.model.game import Game
from web.model.game_web import GameWeb

def domain_to_web(game: Game) -> GameWeb:
    return GameWeb(id=str(game.id), field=game.field.to_list())

def web_to_domain(game_web: GameWeb) -> Game:
    from domain.model.game import Game, GameField
    field = GameField()
    field.matrix = game_web.field
    return Game(uuid.UUID(game_web.id), field)