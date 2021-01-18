class Config():
    #Base flask
    DEBUG = True
    DEVELOPMENT = True
    HOST = '0.0.0.0'
    PORT = '8000'
    
    #DB
    DB_SERVER = 'YOUR_DB_SERVER'
    DB_PORT = 'YOUR_DB_PORT'
    DB_NAME = 'YOUR_DB_NAME'
    DB_USER = 'YOUR_DB_ADMIN'
    DB_PASSWORD = 'YOUR_DB_PASSWORD'

    #line bot
    LINE_CHANNEL_SECRET = '5d909605f87b0a9898ed4a76006b0065'
    LINE_CHANNEL_ACCESS_TOKEN = 'AsLnV8YVl+2+/BTLaHQeAda3jGsaW+0TE5rZwClVwe4OLFL1nuImfSXEfCcJwOQzCEN4HgEAtvetidV0eCdJx5SKzklgUToIDCdGmp/RlHfXeHdJowfMGspGnr+51fth93OrGSMypmKrZ8S9JylZQQdB04t89/1O/w1cDnyilFU='

class ProductionConfig(Config):
    def __init__(self):
        self.DEBUG = False
        self.DB_SERVER = ''
    
class DevelopmentConfig(Config):
    def __init__(self):
        self.DB_SERVER = 'localhost'
        self.DEBUG = True