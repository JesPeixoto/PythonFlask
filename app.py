from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    frutas = ["Morango", "Uva", "Mamão", "Laranja"]
    return render_template("index.html", frutas=frutas)

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

if __name__ == "__main__":
    app.run(debug=True)


#http://127.0.0.1:5000