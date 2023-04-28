import psycopg2
from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

# configurações do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'manager',
    'password': 'manager',
    'database': 'data'
}

# rota GET
@app.route('/registros', methods=['GET'])
def get_registros():
    # conecta ao banco de dados
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # busca os registros no banco de dados
    cursor.execute('SELECT id, nome, idade FROM registros')
    registros = []
    for id, nome, idade in cursor.fetchall():
        registros.append({'id': id, 'nome': nome, 'idade': idade})

    # fecha a conexão com o banco de dados
    cursor.close()
    conn.close()

    response = make_response(jsonify(registros), 200)
    return response

# rota POST
@app.route('/registros', methods=['POST'])
def post_registros():
    # conecta ao banco de dados
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # cadastra o registro no banco de dados
    registro = request.get_json()
    nome = registro['nome']
    idade = registro['idade']
    cursor.execute('INSERT INTO registros (nome, idade) VALUES (%s, %s)', (nome, idade))
    conn.commit()

    # fecha a conexão com o banco de dados
    cursor.close()
    conn.close()

    response = make_response(jsonify(registro), 201)
    return response

# rota DELETE
@app.route('/registros/<int:id>', methods=['DELETE'])
def delete_registro(id):
    # conecta ao banco de dados
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # exclui o registro do banco de dados
    cursor.execute('DELETE FROM registros WHERE id = %s', (id,))
    conn.commit()

    # fecha a conexão com o banco de dados
    cursor.close()
    conn.close()

    response = make_response(jsonify({'message': f'Registro {id} excluído com sucesso'}), 200)
    return response

if __name__ == '__main__':
    app.run(debug=True)