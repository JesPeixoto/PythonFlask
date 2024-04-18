from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    fruta1 = "Morango"
    fruta2 = "Maça"
    fruta3 = "Laranja"
    fruta4 = "Uva"
    return render_template("index.html", 
                           fruta1=fruta1, 
                           fruta2=fruta2, 
                           fruta3=fruta3, 
                           fruta4=fruta4)

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

if __name__ == "__main__":
    app.run(debug=True)


#http://127.0.0.1:5000