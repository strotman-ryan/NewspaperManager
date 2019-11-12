#Flask application for megan

from flask import Flask

application = app = Flask(__name__)


@app.route('/')
def index():
    return "<h1> Hello World for the second time </h1>"

if __name__ == '__main__':
    app.run(debug = True)

