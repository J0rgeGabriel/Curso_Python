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