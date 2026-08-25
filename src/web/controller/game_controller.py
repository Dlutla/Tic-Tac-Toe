"""
Контроллер для работы с игрой: создание новой игры, выполнение хода.
"""
from flask import Blueprint, request, jsonify, current_app
from web.mapper import game_mapper
from domain.service.game_service import GameService
from datasource.repository.game_repository import GameRepository

game_bp = Blueprint('game', __name__, url_prefix='/game')

def get_service() -> GameService:
    return current_app.config['GAME_SERVICE']

def get_repo() -> GameRepository:
    return current_app.config['GAME_REPO']

@game_bp.route('/new', methods=['POST'])
def new_game():
    """Создаёт новую игру и возвращает её JSON."""
    repo = get_repo()
    from domain.model.game import Game
    new_game = Game()
    repo.save(new_game)
    return jsonify(game_mapper.domain_to_web(new_game).__dict__), 201

@game_bp.route('/<uuid:game_id>', methods=['POST'])
def make_move(game_id):
    """
    Обрабатывает ход игрока.
    Ожидает JSON:
    {
        "field": [[...], [...], [...]],
        "player_move": {"row": int, "col": int}
    }
    Возвращает обновлённое поле после хода компьютера.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    
    try:
        field_data = data.get('field')
        player_move = data.get('player_move')
        if not field_data or not player_move:
            return jsonify({"error": "Missing field or player_move"}), 400
        row = player_move.get('row')
        col = player_move.get('col')
        if row is None or col is None:
            return jsonify({"error": "Invalid player_move"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    repo = get_repo()
    if not repo.exists(game_id):
        return jsonify({"error": "Game not found"}), 404

    game = repo.get(game_id)
    service = get_service()

    if not service.validate_move(game, row, col, -1):
        return jsonify({"error": "Invalid move"}), 400

    game.field.set_cell(row, col, -1)

    if service.is_game_over(game):
        repo.save(game)
        return jsonify(game_mapper.domain_to_web(game).__dict__)

    comp_move = service.get_computer_move(game)
    if comp_move != (-1, -1):
        game.field.set_cell(comp_move[0], comp_move[1], 1)

    repo.save(game)
    return jsonify(game_mapper.domain_to_web(game).__dict__)