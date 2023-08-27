quant = int(input("Digite quantos numeros voce deseja na sua lista: "))
i = 1
par = 0 
impar = 0
while i < quant+1:
  num = (int(input("Digite o numero: ")))
  i+=1
  if  num  % 2 ==0:
    par = par + 1
  else:
    impar = impar + 1

print ("A quantidade de numeros pares é: "+str(par))
print ("A quantidade de numeros impar é: "+str(impar))