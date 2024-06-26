# Importa a classe Flask e a função render_template do módulo flask
from flask import Flask, render_template, request
# Cria uma instância da classe Flask e a atribui à variável app
app = Flask(__name__)

frutas = [] # declarando a estrutura de dados no escopo global, para ir add toda vez uma fruta digitada 
registros = []
# Define uma rota padrão para a aplicação
@app.route("/", methods=["GET", "POST"])
def home():
    #frutas = ["Morango", "Uva", "Mamão", "Laranja", "Melão", "Abacaxi"]
    if request.method == "POST":
        if request.form.get("fruta"):
            frutas.append(request.form.get("fruta"))
    return render_template("index.html", frutas=frutas)

# Define uma rota "/sobre" para a aplicação
@app.route("/sobre", methods=["GET", "POST"])
def sobre():
    # notas = {"Alex":7.0, "Monica":8.0, "Alexa":5.0, "Joel":6.5, "Jessica":9.5}
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            registros.append({"aluno": request.form.get("aluno"), "nota": request.form.get("nota")})
            
    return render_template("sobre.html", registros=registros)
# Executa a aplicação se o script estiver sendo executado diretamente
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
    
#http://127.0.0.1:5000