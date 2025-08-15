import os,secrets, getpass
from dotenv import load_dotenv

load_dotenv()

def init_dotenv() -> str:
    if check_envfile() is False:
        with open(".env",'x') as envfile:
            setup_dotenv(envfile)
    return check_env_for_key()
    


def check_env_for_key() -> str:
        """
        Checks .env file for secret key variable, creating a key if not found

        """
        if os.getenv('FLASK_SECRET_KEY') != None:
            return os.getenv('FLASK_SECRET_KEY')
        else:
            with open(".env","a") as envfile:
                key = secrets.token_hex(64)
                envfile.write(f"FLASK_SECRET_KEY= {key}\n")
                envfile.close()
                return os.getenv('FLASK_SECRET_KEY')

def check_envfile():
    return os.path.isfile('./.env')

def setup_dotenv(dotenv):
    port = 3306
    db_name = 'user_db'
    user_name = str(input('Enter Username: '))
    user_pass = getpass.getpass(prompt="Enter Password: ")
    root_pass = getpass.getpass(prompt="Enter Root Password: ")
    
    dotenv.write(f"DB_PORT={port}" " # DO NOT CHANGE \n")
    dotenv.write(f"DB_NAME={db_name}" " # DO NOT CHANGE \n")
    dotenv.write(f"DB_USERNAME={user_name}\n")
    dotenv.write(f"DB_PASSWORD={str(user_pass)}\n")
    dotenv.write(f"ROOT_PASSWORD={str(root_pass)}\n")