#--------------------------------------------------------
#--------------------IMPORTAÇÕES---------------------
#--------------------------------------------------------


from banco import db_contas
from langchain_core.tools import tool

#--------------------------------------------------------
#----------------------ABRIR_CONTA-----------------------
#--------------------------------------------------------




@tool
def abrir_conta(nome, saldo_inicial):
    """
    Cria (abre) uma nova conta bancária. 
    Recebe o 'nome' do cliente (string) e o 'saldo_inicial' (float/int).
    A função verifica se a conta já existe para garantir que não haja duplicidade.
    Retorna uma mensagem de sucesso com o saldo ou uma mensagem de erro se a conta já estiver cadastrada.
    """

    #Padroniza as palavra para ter primeira letra maiscula e o restante minúscula; ex: Ana, Clara, Matheus, etc.
    nome = nome.strip().title()

    saldo = saldo_inicial

    #Verifica se já existe uma conta com esse nome, apesar de que na vida real seria um PK, como CPF, mas só pra ilustração.
    if nome not in db_contas:

        #Adiciona a conta no banco
        db_contas[nome] = {"saldo" : saldo, "historico" : [f"Abertura de conta: +{saldo:.2f}"]}

        #Mensagem de aviso
        return "Conta aberta com sucesso!"
    else:
        #Mensagem de erro
        return "Essa conta já existe"
    





#--------------------------------------------------------
#--------------------ATUALIZAR_SALDO---------------------
#--------------------------------------------------------




@tool
def atualizar_saldo(nome, valor_transaçao):
     
    """
    Atualiza o saldo de UMA conta bancária. 
    Esta função recebe o 'nome' do cliente e o 'valor_transacao' (float/int).

    Depósito/Crédito: Use um valor positivo (+100.00).
    Saque/Débito: Use um valor negativo (-50.00).

    IMPORTANTE: Para TRANSFERÊNCIAS, chame esta função DUAS VEZES: uma para o saque (negativo) e outra para o depósito (positivo).

    Retorna o novo saldo formatado ou a mensagem de erro em caso de saldo insuficiente ou conta inexistente.
    
    """
    
    #Padroniza as palavra para ter primeira letra maiscula e o restante minúscula; ex: Ana, Clara, Matheus, etc.
    nome = nome.strip().title()


    #Verifica se a conta existe no banco.
    if nome in db_contas:
         
        #Pega o saldo da conta pelo nome.
        saldo_atual = db_contas[nome]["saldo"]

        #Faz o cálculo do resultado da transação.
        novo_saldo = saldo_atual + valor_transaçao
         
        #Verifica se transação não é maior que o saldo atual(em caso de transferência ou saque)
        if novo_saldo >= 0:

            #Atualiza o saque 
            db_contas[nome]["saldo"] = novo_saldo

            #Adiciona histórico ao banco
            db_contas[nome]["historico"].append(f"Transação {valor_transaçao:+.2f}")

            #Mensagem de sucesso
            return "Saldo atualizado com sucesso"
         
        else: 
            #Mensagem de erro se o saldo não permitir a transação  
            return "Saldo insuficiente"
         
    else: 
        #Mensagem de erro se a conta não existir no banco
        return "Essa conta não existe!"
        





#--------------------------------------------------------
#---------------------FECHAR CONTAS----------------------
#--------------------------------------------------------




@tool
def fechar_conta(nome) -> str:
    """
    Fecha (deleta) permanentemente uma conta bancária do sistema. 
    Recebe o 'nome' do cliente (string).
    SÓ DEVE SER CHAMADA SE A CONTA EXISTIR E TIVER SALDO IGUAL A ZERO.
    Retorna uma mensagem de sucesso ou uma mensagem de erro se a conta tiver saldo diferente de zero ou não existir.
    """
    #Padroniza as palavra para ter primeira letra maiscula e o restante minúscula; ex: Ana, Clara, Matheus, etc.
    nome = nome.strip().title()

    #Verifica se a conta existe no banco
    if nome in db_contas:

        #Vverifica se ainda existe saldo na conta
        if db_contas[nome]["saldo"] == 0:

            #Deleta a conta do banco
            del db_contas[nome]
            #Mensagem de sucesso
            return f"Conta de {nome} fechada com sucesso"
        
        else:
            #Mensagem de erro se ainda existe saldo na conta
            return f"Ainda existe um saldo de {(db_contas[nome]["saldo"]):.2f} na conta de {nome}, ela não pode ser fechada."
        
    else:
        #Menasgem de erro se a conta não existe no banco
        return "Essa conta não existe no banco"
