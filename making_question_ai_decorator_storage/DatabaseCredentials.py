import os
from making_question_ai_decorator_storage.CheckEnvironmentCredentials import CheckEnvironmentCredentials
from making_question_ai_decorator_storage.MissingConnectionCredentialsError import MissingConnectionCredentialsError

class DatabaseCredentials:
    user: str
    password: str
    host: str
    port: int
    database_name: str
    
    def __init__(self):
        checkEnvironmentCredentials = CheckEnvironmentCredentials()
        if not checkEnvironmentCredentials.is_valid():
            raise MissingConnectionCredentialsError(
                "Missing database connection credentials:\n" +
                checkEnvironmentCredentials.get_errors_string()
            )

        self.user = checkEnvironmentCredentials.get_user()
        self.password = checkEnvironmentCredentials.get_password()
        self.host = checkEnvironmentCredentials.get_host()
        self.port = checkEnvironmentCredentials.get_port()
        self.database_name = checkEnvironmentCredentials.get_database_name()
