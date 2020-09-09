# Set up your imports here!
from flask import Flask 
from flask import request

app = Flask(__name__)

@app.route('/') # Fill this in!
def index():
     return "<h1>Welcome Page</h1> <p> Go to /puppy_latin/name to see the latin name of your pup!</p>"
    # Create a generic welcome page.

@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!
    
    pupname = '' 
    
    if name[-1] != 'y':
        pupname = name+ 'y'
    else:
        pupname = name[:-1] + 'iful'

    return f"Hi {name}! Your puppy latin name is {pupname}"
    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"

if __name__ == '__main__':
    # Fill me in!
    app.run()
