from flask import Flask
import pySql

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.get('/batata')
def login_get():
    res = pySql.buscaAgendamento()
    print(res)
    return res

if __name__ == '__main__':
    app.run()