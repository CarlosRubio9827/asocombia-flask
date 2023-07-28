class Config():
    SECRET_KEY = 'SECRET_KEY'


class DevelopmentConfig(Config):
    DEBUG = True
    # MYSQL_HOST = "localhost"
    # MYSQL_PORT = "3306"
    # MYSQL_USER = "root"
    # MYSQL_PASSWORD = ""
    # MYSQL_DB = "asocombia"


config = {
    'development': DevelopmentConfig
}