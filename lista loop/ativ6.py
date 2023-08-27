num = int(input("Digite quantos números da sequência de Fibonacci você deseja: "))
fibo = []
if num >= 1:
    fibo.append(0)
if num >= 2:
    fibo.append(1)

for i in range(2, num):
    prox_num = fibo[i - 1] + fibo[i - 2]
    fibo.append(prox_num)

print("Os primeiros " +str(num)+ " números da sequência de Fibonacci são: " +str(fibo))