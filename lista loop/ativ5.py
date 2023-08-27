quant = int(input("Digite quantos numeros voce quer na sua lista: "))
i = 1 
numeros = []  

while i < quant + 1:
    num = int(input("Digite o numero: "))
    numeros.append(num) 
    i += 1

maior_num = max(numeros)  
print("O maior numero é:", maior_num)