from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
     return render_template("home.html")

@app.route('/second_page')
def second_page():
     return render_template("second_page.html")

@app.route('/menu')
def menu():
     return render_template("menu.html")

if __name__ == '__main__':
  app.run(debug = True)
