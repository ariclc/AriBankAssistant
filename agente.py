from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

from banco import listar_todas_contas,buscar_saldo
from crud import abrir_conta, atualizar_saldo, fechar_conta

from config import GOOGLE_API_KEY
import os


os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

tools = [listar_todas_contas, buscar_saldo, abrir_conta,atualizar_saldo, fechar_conta]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash")




bank_system_prompt = """
Você é um assistente bancário útil e seguro, projetado para gerenciar contas de clientes.
Seu nome é Ari a Bank Assitent. Você só pode interagir com o sistema usando as ferramentas fornecidas.
Sempre retorne uma resposta clara, amigável e em português.
Não pessa confirmação do usuário apenas realize as operações que ele quer.
"""

ari = create_react_agent(
    llm,
    tools = [listar_todas_contas, buscar_saldo, abrir_conta,atualizar_saldo, fechar_conta],
    prompt = bank_system_prompt,
    )


def falar_com_agente(texto):
  conversa = ari.invoke({
      "messages": [
          ("human", texto)
      ]
  })

  return conversa ['messages'][-1]