num = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

if num < 0:
  print("Não está definido para números negativos.")
elif num == 0:
  print("O fatorial de 0 é 1.")
else:
  for i in range(1, num + 1):
    fatorial *= i

print("O fatorial de "+str(num)+" é "+str(fatorial))