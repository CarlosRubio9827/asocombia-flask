class Config():
    SECRET_KEY = 'SECRET_KEY'


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig
}