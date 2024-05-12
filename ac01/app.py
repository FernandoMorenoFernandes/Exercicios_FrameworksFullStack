from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'AC01'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)


@app.route('/')
def contato():
    return render_template('index.html')


@app.route('/gravar', methods=['POST', 'GET'])
def gravar():
    try:
        _nome = request.form['nome']
        _endereco = request.form['endereco']
        _telefone = request.form['telefone']

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into tbl_cadastro (user_name, user_endereco, user_telefone) VALUES (%s, %s, %s)',
                       (_nome, _endereco, _telefone))
        conn.commit()

        return "Dados gravados com sucesso!"  # Adicionando uma resposta de sucesso

    except Exception as e:
        return str(e)  # Retornando uma mensagem de erro se houver algum problema
        
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
