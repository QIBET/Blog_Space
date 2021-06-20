import os


class Config:
    '''
    General parent class for configuration
    '''

    
    SECRET_KEY=os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS =True

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

   #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: General parent class for configuration
    '''
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL"," ")
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1) 
        
   
class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings 
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: General parent class for configuration
    '''
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://moringa:Sotik2020*@localhost/blogspace"
    
    
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
}
