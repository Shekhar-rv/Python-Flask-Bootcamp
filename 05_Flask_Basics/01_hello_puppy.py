from flask import Flask

# Create a instance of Flask
app = Flask(__name__)

# Create a route with a function
@app.route('/')
def index():
    return "<h1>Hello Puppy!</h1>"

# Run the app
if __name__ == '__main__':
    app.run()