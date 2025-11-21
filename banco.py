#--------------------------------------------------------
#--------------------IMPORTAÇÕES---------------------
#--------------------------------------------------------


from langchain_core.tools import tool


#--------------------------------------------------------
#-------------------------BANCO--------------------------
#--------------------------------------------------------



#Banco com algumas contas pré definidas
db_contas = {
    "João": {"saldo": 1000.00, "historico": ["Abertura de conta: +1000.00"]},
    "Maria": {"saldo": 500.50, "historico": ["Abertura de conta: +500.50"]},
    "Carlos": {"saldo": 750.00, "historico": ["Abertura de conta: +750.00"]}
    }




#--------------------------------------------------------
#----------------------BUSCA SALDO-----------------------
#--------------------------------------------------------



@tool
def buscar_saldo(nome: str) -> str:
    """
    Busca e retorna o saldo atual de uma conta específica. 
    Esta é uma operação de CONSULTA (READ) e NÃO modifica o saldo.
    Recebe o 'nome' do cliente (string).
    Retorna uma mensagem de sucesso com o saldo formatado (ex: R$ 1000.00) 
    ou uma mensagem de erro se a conta não for encontrada.
    """

    #Padroniza as palavra para ter primeira letra maiscula e o restante minúscula; ex: Ana, Clara, Matheus, etc.
    nome= nome.strip().title()

    #Verifica se cliente está no banco
    if nome in db_contas:

        #Acessa o dicionário e pega o saldo
        saldo = db_contas[nome]["saldo"]

        #retorna a mensagem formatada
        return f"O saldo atual da conta de {nome}é de R${saldo:.2f}."

    else:
        #Caso cliente não esteja no banco, retorna a mensagem de erro.
        return f"A conta de {nome}não foi encontrada."
    




#--------------------------------------------------------
#-----------------LISTAR TODAS AS CONTAS-----------------
#--------------------------------------------------------



@tool
def listar_todas_contas() -> str:

    """
    Gera um relatório completo com o nome de TODOS os clientes e seus saldos atuais.
    Esta é uma operação de CONSULTA (READ) e NÃO requer parâmetros.
    Retorna uma string formatada, listando cada cliente com seu saldo.
    Se não houver contas, retorna uma mensagem de aviso.
    """

    relatorio = "Contas Cadastradas:\n"

    for nome, dados in db_contas.items():
        #Pega os saldos do banco
        saldo = dados["saldo"]

        #adiciona uma linha formatada no final do relatório toda vez que passa no laço
        relatorio += f"-Cliente: {nome}, Saldo: R$ {saldo:.2f}\n"
    #retorna a lista completa no final
    return relatorio