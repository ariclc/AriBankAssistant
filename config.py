import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='key.env')

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

if GOOGLE_API_KEY is None:
    raise ValueError("A variável GOOGLE_API_KEY não foi encontrada no arquivo key.env.")