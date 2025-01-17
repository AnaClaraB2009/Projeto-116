# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = " Ana Clara " 
    idade = " 14 anos " # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("pai")
def home():

    nome = " Andre  " 
    idade = " 43 anos " # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)


# defina a rota para a página da mãe
@app.route("mae")
def home():

    nome = " Manoela " 
    idade = " 44 anos " # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)


# defina a rota para a página do amigo
@app.route("amigo")
def home():

    nome = " Lilian " 
    idade = " 15 anos " # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)


# adicione outras rotas, se você quiser




# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
