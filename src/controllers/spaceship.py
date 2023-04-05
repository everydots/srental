from flask import jsonify, request
from . import bp
from ..services.contract import parse_contract_json, get_optimal_contracts


@bp.route('/spaceship/optimize', methods=['POST'])
def optimize_spaceship():
    request_data = request.get_json()
    contracts = parse_contract_json(request_data)
    optimal_contracts, max_profit = get_optimal_contracts(contracts)
    optimal_contract_names = [contract.name for contract in optimal_contracts]
    return jsonify({'income': max_profit, 'path': optimal_contract_names})
