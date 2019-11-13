#Flask application for megan

from app import create_app


application = app = create_app('default')

if __name__ == "__main__":
    app.run()

