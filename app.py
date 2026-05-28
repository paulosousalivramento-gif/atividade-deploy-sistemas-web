from flask import Flask, render_template, request, redirect, url_url

app = Flask(__name__)

# Lista inicial com as 3 tarefas originais do print
tarefas = [
    {"nome": "Configurar o ambiente Python", "concluida": True},
    {"nome": "Desenvolver o Front-end e Back-end", "concluida": True},
    {"nome": "Fazer o deploy da aplicação", "concluida": False}
]

@app.route('/')
def index():
    return render_template('index.html', tarefas=tarefas)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome_tarefa = request.form.get('nome')
    if nome_tarefa:
        tarefas.append({"nome": nome_tarefa, "concluida": False})
    return redirect('/')

@app.route('/alternar/<int:indice>')
def alternar(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]['concluida'] = not tarefas[indice]['concluida']
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
