from models.produto_models import Notebook    
from db import db                        
import json                               
from flask import make_response

def create_notebook(notebook_data):
    novo_notebook = Notebook(
        nome=notebook_data['nome'],
        categoria=notebook_data['categoria'],
        preco=notebook_data['preco']
    )
    db.session.add(novo_notebook)
    db.session.commit()
response = make_response(            
        json.dumps({                      
            'mensagem': 'Produto cadastrado com sucesso!',  
            'produto': novo_produto.json()
        }, sort_keys=False)
    )
    response.headers['content-Type'] = 'application/json'
    return response