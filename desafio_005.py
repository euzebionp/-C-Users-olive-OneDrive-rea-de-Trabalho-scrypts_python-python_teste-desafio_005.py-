# faça um programa que leia um número inteiro e mostre seu sucessor e seu antecessor.

print('='*5, ' Desafio 005 ', '='*5)

nome = input('Digite o nome do aluno: ')
print('Bem vindo {}'.format(nome), ',vamos fazer o exercício ?')

print('5- Escolha um número inteiro para descobrir seu sucessor e seu antecessor.')

ni = int(input('Digite im número inteiro: '))
su = ni + 1
ant = ni - 1
# resposta exercício 5
print(' R - O número digitado foi {}, o seu sucessor é {} e seu antecessor é {}, respectivamente !!!'.format(ni, su, ant))

# Crie um algorítimo que leia um número e mostre o seu dobro, o triplo e a raiz quadrada

print('6- Escolha um número inteiro para descobrir o dobro, triplo e a raiz quadrada ')

n = int(input('Digite um numero: '))
do = n * 2
tri = n * 3
rz = n * 1/2
# resposta exercício 6
print(' R- O número digitado foi {}, seu dobro é {}, seu triplo é {} e sua raiz é {: .0f}'.format(n, do, tri, rz), ', respectivamente !!!') 

# Desenvolva um programa que laia a s duas notas de um aluno, calcule e mostre sua média 

aluno2 = input('Digite o nome do aluno: ')
nota_1 = int(input('Digite a nota_1: '))
nota_2 = int(input('Digite a nota_2: '))
soma = int(nota_1) + int(nota_2) 
media = soma / 2

print('A media das notas do aluno {} é {}'.format(aluno2,media ))


 
