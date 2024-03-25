import os
from dotenv import load_dotenv

class Config:

    def __init__(self):
        dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')

        if not os.path.exists(dotenv_path):
            raise Exception("Don't has .env file. Added .env file with required environments.")

        load_dotenv(dotenv_path)

        try:
            self.db_host = os.environ.get('DB_HOST').strip()
            self.db_port = int(os.environ.get('DB_PORT').strip())
            self.db_user = os.environ.get('DB_USER').strip()
            self.db_password = os.environ.get('DB_PASSWORD').strip()
            self.db_name = os.environ.get('DB_NAME').strip()

            is_has1 = not self.db_host or not self.db_port or not self.db_user
            is_has2 = not self.db_password or not self.db_name

            if is_has1 or is_has2:
                raise Exception('')
        except:
            raise Exception('Invalid .env file. It is necessary to fix errors and unspecified environment variables.')


    def get_database_url(self) -> str:
        return f'postgres://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}'