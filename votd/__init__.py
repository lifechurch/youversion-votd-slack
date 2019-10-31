import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

print(os.getenv('YOUVERSION_KEY'))