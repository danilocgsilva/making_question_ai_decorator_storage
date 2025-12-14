import os

class DatabaseCredentials:
    def __init__(self):
        self.user = os.getenv('MYSQL_USER')
        self.password = os.getenv('MYSQL_PASSWORD')
        self.host = os.getenv('MYSQL_HOST')
        self.port = int(os.getenv('MYSQL_PORT', 3306))
        self.database = os.getenv('MYSQL_DATABASE')
