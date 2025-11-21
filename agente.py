#--------------------------------------------------------
#----------------------IMPORTAÇÕES-----------------------
#--------------------------------------------------------



# Importações de Bibliotecas (LangChain, LangGraph, os)
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
import os

# Importações de Ferramentas (Tools) e Configuração Local
from banco import listar_todas_contas,buscar_saldo
from crud import abrir_conta, atualizar_saldo, fechar_conta
from config import GOOGLE_API_KEY




#--------------------------------------------------------
#---------------CONFIGURAÇÃO E INICIALIZAÇÃO LLM---------
#--------------------------------------------------------





#Carrega a chave do arquivo config e e define a chave 
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

#lista de tools para llm
tools = [listar_todas_contas, buscar_saldo, abrir_conta,atualizar_saldo, fechar_conta]

#inicia a llm do gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash")






#--------------------------------------------------------
#-----------------PROMPT E CRIAÇÃO DO AGENTE-------------
#--------------------------------------------------------






#Cria um prompt pra orientar o comportamento da llm no ambiente
bank_system_prompt = """
Você é um assistente bancário útil e seguro, projetado para gerenciar contas de clientes.
Seu nome é Ari a Bank Assitent. Você só pode interagir com o sistema usando as ferramentas fornecidas.
Sempre retorne uma resposta clara, amigável e em português.
Não pessa confirmação do usuário apenas realize as operações que ele quer.
"""

#Cria o bot e configura as tools
ari = create_react_agent(
    llm,
    tools = [listar_todas_contas, buscar_saldo, abrir_conta,atualizar_saldo, fechar_conta],
    prompt = bank_system_prompt,
    )





#--------------------------------------------------------
#-----------------FUNÇÕES DE COMUNICAÇÃO-----------------
#--------------------------------------------------------






#função pra facilitar a chamada do bot
def falar_com_agente(texto):
  
  #inicia o bot e manda as mensagem encapsuladas da estrutura definida
  conversa = ari.invoke({
      "messages": [
          ("human", texto)
      ]
  })
  
  #essa linha extrai a resposta final que vai ser xibida pra o usuário
  return conversa ['messages'][-1]