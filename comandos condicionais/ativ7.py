x = float(input("Digite a coordenada x do ponto: "))
y = float(input("Digite a coordenada y do ponto: "))

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
elif x == 0 and y == 0:
    print("O ponto está na origem.")
else:
    print("O ponto está sobre um dos eixos.")