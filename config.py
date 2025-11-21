#--------------------------------------------------------
#----------------------IMPORTAÇÕES-----------------------
#--------------------------------------------------------

import os
from dotenv import load_dotenv


#--------------------------------------------------------
#-----------------CONFIGURAÇÃO DE SEGURANÇA--------------
#--------------------------------------------------------



#Carrega as variaveis definidas no arquivo key.env
load_dotenv(dotenv_path='key.env')

#procurar a variável chamada "GOOGLE_API_KEY"
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

#verifica se existe uma chave no arquivo key.env
if GOOGLE_API_KEY is None:
    raise ValueError("A variável GOOGLE_API_KEY não foi encontrada no arquivo key.env.")