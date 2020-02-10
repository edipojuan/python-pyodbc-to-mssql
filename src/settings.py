from dotenv import load_dotenv
from os import getenv

load_dotenv(verbose=True)

SERVER = getenv('SERVER')
DATABASE = getenv('DATABASE')
LOGIN = getenv('LOGIN')
PASSWORD = getenv('PASSWORD')
