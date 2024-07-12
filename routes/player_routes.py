from flask import Blueprint
from controllers.player_controller import (
    get_all_players,
    get_player,
    create_player,
    update_player,
    delete_player
)

player_bp = Blueprint('player', __name__)

@player_bp.route('/players', methods=['GET'])
def get_players():
    return get_all_players()

@player_bp.route('/player/<player_id>', methods=['GET'])
def get_single_player(player_id):
    return get_player(player_id)

@player_bp.route('/player', methods=['POST'])
def post_player():
    return create_player()

@player_bp.route('/player/<player_id>', methods=['PUT'])
def put_player(player_id):
    return update_player(player_id)

@player_bp.route('/player/<player_id>', methods=['DELETE'])
def delete_single_player(player_id):
    return delete_player(player_id)
