from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/o-mnie-marta-bucholc")
def subpage1():
    return render_template("oMnie.html")

@app.route("/kontakt")
def subpage2():
    return render_template("kontakt.html")

@app.route("/cennik")
def subpage3():
    return render_template("cennik.html")

@app.route('/dlaczego-terapia-wazna')
def subpage4():
    return render_template("terapia.html")

@app.route('/empty')
def subpage5():
    return render_template('empty.html')

if __name__ == "__main__":
    app.run(debug=True)
