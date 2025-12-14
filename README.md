# Storage Decorator for making question

## Environment Variables for MySQL Connection

Set the following variables in your environment (e.g. in a `.env` file or in your deployment environment) before running the app:

```sh
MYSQL_USER=<your_mysql_user>
MYSQL_PASSWORD=<your_mysql_password>
MYSQL_HOST=<mysql_host>
MYSQL_PORT=3306
MYSQL_DATABASE=<mysql_database>
```

SQLAlchemy is configured in `making_question_ai_decorator_storage/db.py` to connect using these variables.

## Alembic Usage

When running Alembic migrations, make sure the environment variables are set so that Alembic uses the correct connection string.

```sh
MYSQL_USER=... MYSQL_PASSWORD=... MYSQL_HOST=... MYSQL_PORT=... MYSQL_DATABASE=... alembic upgrade head
```

Alternatively, you can edit the `alembic.ini` for a hardcoded connection string, but using environment variables is recommended for security and flexibility.

To run migrations, first create a database.

Then, ensure that the requirements packages are installed (check `requirements.txt`), then in the project root, run:
```
alembic upgrade head
```

