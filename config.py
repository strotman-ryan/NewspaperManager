#config.py

#import os

#basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    
    #SECRET_KEY = os.environ.get('MEGAN_NEWSPAPER_SECRET_KEY') or "asdhfos9d8h970qw4987qr49qr8uehfasl"
    SECRET_KEY = "asdhfos9d8h970qw4987qr49qr8uehfasl"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://admin:Gc6TxzXkk2c6rZ5QTHBP@newspaper.cokfefeylfto.us-east-1.rds.amazonaws.com/test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @staticmethod
    def init_app(app):
        pass
    
config = {
        'default' : Config
        }