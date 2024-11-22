from flask import Blueprint, jsonify
from app.repositories.unko import UnkoRepository  

bp = Blueprint('api', __name__)

@bp.route('/unkos', methods=['GET'])
def get_all_unkos():
    try:
        unkos = UnkoRepository.get_unkos()
        unkos_list = [unko for unko in unkos]
        return jsonify(unkos_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/unkos', methods=['GET'])
