#--------------------------------------------------------
#----------------------IMPORTAÇÕES-----------------------
#--------------------------------------------------------


from agente import falar_com_agente

#--------------------------------------------------------
#------------------Configura interface-------------------
#--------------------------------------------------------



print("\n"*30 + "="*50) # Adiciona uma linha superior
print("🤖 Ari Bank Assistent Iniciado 💰")
print("="*50)

print("Digite 'sair' para encerrar a sessão.")
print("\n")



#--------------------------------------------------------
#------------------INICIALIZAÇÃO DO BOT------------------
#--------------------------------------------------------



while True:
    texto = input("Você: ")

    #padroniza texto pra não ter erro quando user pedir pra encerrar e encerra o bot quebrando o laço
    if texto.lower() == "sair":
        print("Encerrando...")
        break
    
    #chama a função do arquivo agente
    resposta_objeto = falar_com_agente(texto)

    #Organiza saída do texto da Ari
    print("Ari: ", resposta_objeto.content)