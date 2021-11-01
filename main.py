import pprint

from flask import Flask, render_template
import requests

app = Flask(__name__)

npoint = "https://api.npoint.io/88c2c1f644ef334058be"
respond = requests.get(npoint)
result = respond.json()

pprint.pprint(result)

@app.route('/')
def main():
    return render_template("index.html", data=result)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/<int:id>')
def post(id):
    for post in result:
        if id == post["id"]:
            return render_template("post.html", data=post)

if __name__ == '__main__':
    app.run(debug=True)
