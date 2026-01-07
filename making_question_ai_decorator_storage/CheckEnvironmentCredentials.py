import os

class CheckEnvironmentCredentials:
    databaseUser = None
    databasePassword = None
    databaseHost = None
    databaseName = None
    databasePort = 3306
    
    def __init__(self):
        errors = []
        if not os.getenv('MYSQL_USER'):
            errors.append("Environment variable MYSQL_USER is not set.")
        if not os.getenv('MYSQL_PASSWORD'):
            errors.append("Environment variable MYSQL_PASSWORD is not set.")
        if not os.getenv('MYSQL_HOST'):
            errors.append("Environment variable MYSQL_HOST is not set.")
        if not os.getenv('MYSQL_DATABASE'):
            errors.append("Environment variable MYSQL_DATABASE is not set.")
            
    def is_valid(self):
        return len(errors) == 0
    
    def get_errors_string(self):
        return "\n".join(errors)
    
    def getDatabaseUser(self):
        return self.databaseUser
    
    def getDatabasePassword(self):
        return self.databasePassword
    
    def getDatabaseHost(self):
        return self.databaseHost
    
    def getDatabaseName(self):
        return self.databaseName
    
    def getDatabasePort(self):
        return self.databasePort
