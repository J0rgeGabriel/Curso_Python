"""
for c in range (0,7,2):
    print(c)
print('FIM')
#se for apresentar o numero de forma decrescente faça: (6,0,-1)
#caso queira fazer apresentar numeros de 2 em 2 faça: (0,7,2)
"""
"""
for andar in range (0,10001,500):
    print(andar)
print("Voce chegou ao seu destino")
"""
"""
i = int(input('Inicio: '))  #onde começa
f = int(input('Fim: '))     #onde termina
p = int(input('Passo: '))   #de quantos em quantos passo ele ira do começo ao fim

for c in range (i,f+1,p):
    print(c)
print('FIM')
"""
"""
soma = 0
for contador in range(0, 4):
    nota = int(input('Digite sua nota: '))
    soma += nota

if soma < 10:
    print(f"A soma das notas é: {soma}, foi REPROVADO!!")
else:
    print(f"A soma das notas é: {soma}, foi APROVADO!!")
"""
"""
#Ex01:
#Faça um programa que mostra na tala uma contagem regrassiva,i ndo de 10 até O, com uma pausa de segundo entre elas.

for contagem in range(10,0,-1):
    print(contagem)
    time.sleep(1)           #time.sleep(1) pausa o programa por 1 segundo antes de continuar para a próxima
print("🎆🎆🎆🎆")
"""
"""
#Ex2:
#Crie um programa qua mostra na tala todos os numeros pares que estao no intervalo antre 1 a 50:

for n in range (0,50,2):
    print(n)
"""
"""
#Ex03:
#Faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de 3 que estão entre 1 e 500:
soma = 0
for n in range(0,500):
    if n %2 != 0 and n %3 == 0:
       soma += n
print(soma)
#n % 2 calcula o resto da divisão de n por 2. Se o resto for diferente de zero, então n é ímpar.
#n % 3 calcula o resto da divisão de n por 3. Se o resto for igual a zero, então n é divisível por 3.
"""
"""
#Ex04:
#Faça um programa que leia 6 numeros inteiros e mostre a soma dos numeros pares:
soma = 0
for n in range (0,6):
    numerosINT = int(input('Digite um numero inteiro'))
    if numerosINT %2 == 0:
        soma += numerosINT
print(f"A soma dos numeros pares é {soma}")
"""