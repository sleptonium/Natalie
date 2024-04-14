""" Hello World flask app for learning"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    " Return Hello World"

    return 'Hello, World!'

@app.route('/natalie')
def natalie():
    " Return Hello Natalie"

    return 'Hello, Natalie!'

# create a page which takes a number from the user and returns all it's prime factors
@app.route('/prime_factors/<int:n>')
def get_prime_factors(n):
    "Return prime factors of n"
    return f"Prime factors of {n} are {prime_factors(n)}"


# Creat a functiom that takes a number and returns all it's prime factors
def prime_factors(n):
    "Return prime factors of n"
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
  

if __name__ == '__main__':
    app.run(debug=True)
