from agente import falar_com_agente


print("\n" + "="*50) # Adiciona uma linha superior
print("🤖 Ari Bank Assistent Iniciado 💰")
print("="*50)

print("Digite 'sair' para encerrar a sessão.")
print("\n")

while True:
    texto = input("Você: ")

    if texto.lower() == "sair":
        print("Encerrando...")
        break

    resposta_objeto = falar_com_agente(texto)

    print("Ari: ", resposta_objeto.content)