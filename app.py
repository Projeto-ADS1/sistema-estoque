from flask import Flask, render_template, request, jsonify
import os
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Configuração da Conexão com o MySQL Workbench
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST','localhost'),
            database=os.getenv ('DB_NAME','estoque'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', 'Slsql#0306')  # <-- Coloque sua senha do MySQL Workbench aqui
        )
        return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

# Rotas de Categorias
@app.route('/api/categorias', methods=['GET', 'POST'])
def gerenciar_categorias():
    conn = get_db_connection()
    if not conn:
        return jsonify({'erro': 'Erro de conexão com o banco'}), 500
    
    cursor = conn.cursor(dictionary=True)

    if request.method == 'GET':
        cursor.execute("SELECT * FROM categoria")
        categorias = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(categorias)

    if request.method == 'POST':
        dados = request.get_json()
        nome = dados.get('nome')
        try:
            cursor.execute("INSERT INTO categoria (nome) VALUES (%s)", (nome,))
            conn.commit()
            cat_id = cursor.lastrowid
            return jsonify({'id': cat_id, 'nome': nome}), 201
        except mysql.connector.Error as err:
            return jsonify({'erro': str(err)}), 400
        finally:
            cursor.close()
            conn.close()

# Rotas de Produtos
@app.route('/api/produtos', methods=['GET', 'POST'])
def gerenciar_produtos():
    conn = get_db_connection()
    if not conn:
        return jsonify({'erro': 'Erro de conexão com o banco'}), 500
    
    cursor = conn.cursor(dictionary=True)

    if request.method == 'GET':
        cursor.execute("SELECT * FROM produto")
        produtos = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(produtos)

    if request.method == 'POST':
        dados = request.get_json()
        try:
            cursor.execute(
                """INSERT INTO produto (sku, nome, preco, quantidade, categoria_id) 
                   VALUES (%s, %s, %s, %s, %s)""",
                (dados.get('sku'), dados.get('nome'), dados.get('preco'), 
                 dados.get('quantidade'), dados.get('categoria_id'))
            )
            conn.commit()
            prod_id = cursor.lastrowid
            return jsonify({'id': prod_id, **dados}), 201
        except mysql.connector.Error as err:
            return jsonify({'erro': str(err)}), 400
        finally:
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)