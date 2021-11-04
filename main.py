import pprint
from flask import Flask, render_template, request
import requests
from msg import send_email

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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html", send_message=False)
    elif request.method == 'POST':
        name = request.form['name']
        print(name)
        email = request.form['email']
        print(email)
        phone = request.form['phone']
        print(phone)
        message = request.form['message']
        print(message)
        send_email(name=name, email=email, phone=phone, message=message)
        return render_template("contact.html", send_message=True)
    else:
        return f"<h1>ERROR!!!<h1>"

@app.route('/<int:id>')
def post(id):
    for post in result:
        if id == post["id"]:
            return render_template("post.html", data=post)

"""
@app.errorhandler(404)
def not_found():
    return render_template('error.html'), 404
"""

if __name__ == '__main__':
    app.run(debug=True)
