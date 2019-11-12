#Flask application for megan

from flask import Flask, render_template

application = app = Flask(__name__)


@app.route('/')
def index():
    return render_template('framework.html')

if __name__ == '__main__':
    app.run(debug = True)

