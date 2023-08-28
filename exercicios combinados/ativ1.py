notas = []
continuar = True

while continuar:
    entrada = (input("Digite a nota do aluno (oustop para parar): "))
    
    if entrada == "stop":
        continuar = False
    else:
        nota=float(entrada)
        notas.append(nota)

if notas:
    media = sum(notas) / len(notas)
    print("A média das notas é:"+str(media))
else:
    print("Nenhuma nota foi inserida.")