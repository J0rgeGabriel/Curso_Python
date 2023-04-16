'''
for c in range (1,10):
    print(c)
print("FIM")
'''
"""
c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')
"""
'''
r = "S"
while r == "S":
    n = int(input("Digite um valor:  "))
    r = str(input("Quer continuar? [S/N]")).upper()
print("FIM")
'''
"""
n = 1
par = 0
impar = 0

while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n %2 == 0:
            par += 1
        else:
            impar += 1

print(f"Você digitou {par} números pares e {impar} números impares")
"""
'''
#Ex01:
#Faça um programa que leia o sexo de uma pessoa mas so aceite M ou F. Caso esteja errado peça para digitar novamente:
sexo = input("Digite o seu sexo [M/F]: ").upper()
while sexo not in ("M/F"):
    sexo = input("Sexo invalido, digite novamente o seu sexo [M/F]: ").upper()
print(f"Sexo registrado: {sexo}")
'''
'''
while True:     #o comando While True: é uma estrutura de repetição que cria um loop infinito.
    print("Loop infinito!")
'''
'''
while True:
    for x in range(1,6):
        print(x)
'''

while True:
    n1 = float(input("Digite o primeiro numero: "))
    n2 = float(input("Digite o segundo numero: "))
    opcao = input("Escolha uma opção:\n"
                  "1 - Somar\n"
                  "2 - multiplicar\n"
                  "3 - maior \n"
                  "4 - novos numeros\n"
                  "5 - sair do programa")

    if opcao == "1":
        total = n1 + n2
        print(f"A soma do primeiro numero + o segundo numero é {total}")

    elif opcao == "2":
        total = n1 * n2
        print(f"A multiplicação do primeiro numero com o segundo numero é {total}")

    elif opcao == "3":
        if n1 > n2:
            print(f"O numero {n1} é maior que {n2}")
        else:
            print(f"O numero {n2} é maior que {n1}")

    elif opcao == "4":
        continue #volta ao inicio do loop

    elif opcao == "5":
        print("Saindo do programa")
        break

    else:
        print("Opção inválida, tente novamente.")
print("\n")
print("Fim do programa.")
