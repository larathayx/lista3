numeros = []

while True:
    entrada = input("Digite um número (ou stop para encerrar): ")
    
    if entrada == 'stop':
        break
    
    numero = float(entrada)
    numeros.append(numero)

if numeros:
    menor_valor = min(numeros)
    print("O menor valor é: "+str(menor_valor) )
else:
    print("Nenhum número foi inserido.")