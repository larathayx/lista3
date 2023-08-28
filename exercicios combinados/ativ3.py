numeros_para_adivinhar = [27, 14, 88, 42, 67, 5, 73, 20, 59, 91]
indice_atual = 0
tentativas = 0

print("Bem-vindo ao Jogo de Adivinhação!")
print("Tente adivinhar o próximo número na sequência.")

while indice_atual < len(numeros_para_adivinhar):
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1
    
    if palpite == numeros_para_adivinhar[indice_atual]:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        indice_atual += 1
    else:
        print("Tente novamente.")

print("Você adivinhou todos os números da sequência!")