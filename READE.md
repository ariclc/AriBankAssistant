# 🤖 Ari Bank Assistent 💰

Assistente bancário conversacional construído com o framework LangChain e LangGraph, utilizando o modelo Gemini 2.5 Flash para processamento de linguagem natural e orquestração de ferramentas (tools) Python para simular operações bancárias.



-------------------------------------------------------------
-------------------------------------------------------------
-------------------------------------------------------------



## 🌟 Funcionalidades

O Ari pode realizar as seguintes operações através da interface conversacional:

| Operação | Ferramenta (Tool) | Descrição |
| :--- | :--- | :--- |
| **CREATE** | `abrir_conta` | Cria uma nova conta bancária com nome e saldo inicial. |
| **READ** | `listar_todas_contas` | Retorna a lista completa de clientes e seus saldos. |
| **READ** | `buscar_saldo` | Retorna o saldo atual de um cliente específico. |
| **UPDATE** | `atualizar_saldo` | Realiza depósitos, saques e transferências (em dois passos). |
| **DELETE** | `fechar_conta` | Fecha uma conta, mas apenas se o saldo for zero. |



-------------------------------------------------------------
-------------------------------------------------------------
-------------------------------------------------------------



## ⚙️ Pré-requisitos

* Python 3.10+
* Chave de API do Google AI Studio (Gemini API Key)



-------------------------------------------------------------
-------------------------------------------------------------
-------------------------------------------------------------



## 📦 Instalação

Siga os passos abaixo para configurar e rodar o projeto.


### 1. Criar e Ativar Ambiente Virtual

Recomendamos usar um ambiente virtual para isolar as dependências:


# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente virtual (Windows PowerShell)
.\venv\Scripts\activate



-------------------------------------------------------------
-------------------------------------------------------------
-------------------------------------------------------------



2. Instalar Dependências
Com o ambiente virtual ativado, instale todas as bibliotecas necessárias:

pip install langchain-google-genai langchain langchain-core langgraph python-dotenv



-------------------------------------------------------------
-------------------------------------------------------------
-------------------------------------------------------------



🔑 Configuração da API
O projeto utiliza a biblioteca python-dotenv para carregar sua chave de API de um arquivo key.env por segurança.

Crie um arquivo chamado key.env na pasta raiz do projeto (C:\BankAssistent).

Dentro do arquivo key.env, adicione sua chave de API no formato abaixo:

GOOGLE_API_KEY="SUA_CHAVE_GEMINI_AQUI"



-------------------------------------------------------------
-------------------------------------------------------------
-------------------------------------------------------------



▶️ Como Rodar
Com o ambiente virtual ativado e a chave configurada

Instale as dependências necessárias dentro do ambiente virtual, então execute o script principal:

python main.py



-------------------------------------------------------------
-------------------------------------------------------------
-------------------------------------------------------------



💬 Exemplos de Uso

Criar Conta: "cria uma conta pra João Silva com 1000 de saldo"

Verificar Saldo: " qual o saldo de Maria Clara?"

Depositar: "eu quero depositar 500 reais na minha conta"

Transferir: "transfere 200 de João para Maria"

Listar Contas: "lista todas as contas pra mim"

Fechar Conta: "delete a conta de Mariana"



-------------------------------------------------------------
-------------------------------------------------------------
-------------------------------------------------------------



## ⚠️ Aviso Importante: Estado do Sistema

**ESTE É UM SISTEMA DE TESTES (IN-MEMORY):**

O assistente Ari gerencia as contas em um dicionário Python que reside apenas na **memória RAM** do seu computador.

**Isso significa que, se você encerrar o programa (`python main.py`) e iniciá-lo novamente, todos os dados criados (novas contas, saldos alterados, etc.) serão perdidos e o dicionário será resetado para o estado inicial.**