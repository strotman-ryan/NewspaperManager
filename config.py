#config.py

#import os

#basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    
    #SECRET_KEY = os.environ.get('MEGAN_NEWSPAPER_SECRET_KEY') or "asdhfos9d8h970qw4987qr49qr8uehfasl"
    SECRET_KEY = "asdhfos9d8h970qw4987qr49qr8uehfasl"
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @staticmethod
    def init_app(app):
        pass
    
config = {
        'default' : Config
        }