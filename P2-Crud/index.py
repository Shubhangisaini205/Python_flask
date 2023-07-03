
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the Flask application!!'

@app.route('/greet/<username>')
def greet_user(username):
    return f'Hello, {username}!'

@app.route('/greet/<username>/<int:age>')
def greet_user(username, age):
    location = request.args.get('location')
    message = f'Hello, {username}! You are {age} years old.'
    if location:
        message += f' You are located in {location}.'
    return message

@app.route('/farewell/<username>')
def farewell_user(username):
    return f'Goodbye, {username}!'


if __name__ == '__main__':
    app.run(debug=True,port=8000)

