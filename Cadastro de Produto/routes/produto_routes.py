from flask import Blueprint, request
from controllers.produto_controllers import create_notebook

produto_routes = Blueprint('produto_routes', __name__)

@produto_routes.route('/Notebook', methods=['POST'])
def produto_post():
    produto_data = request.json
    return create_produto(request.json)