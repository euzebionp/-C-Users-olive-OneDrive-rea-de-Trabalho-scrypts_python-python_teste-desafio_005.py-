# faça um programa que leia um número inteiro e mostre seu sucessor e seu antecessor.
while True:
    print('='*5, ' Desafio 005 ', '='*5)

    nome = input('Digite o nome do aluno: ')
    print('Bem vindo {}'.format(nome), ',vamos fazer o exercício ?')

    print('5- Escolha um número inteiro para descobrir seu sucessor e seu antecessor.')

    ni = int(input('Digite um número inteiro: '))
    su = ni + 1
    ant = ni - 1
    # resposta exercício 5
    print(' R - O número digitado foi {}, o seu sucessor é {} e seu antecessor é {}, respectivamente !!!'.format(ni, su, ant))

    # Crie um algorítimo que leia um número e mostre o seu dobro, o triplo e a raiz quadrada

    print('6- Escolha um número inteiro para descobrir o dobro, triplo e a raiz quadrada ')

    n = int(input('Digite um numero: '))
    do = n * 2
    tri = n * 3
    rz = n ** (1/2)
    # resposta exercício 6
    print(' R- O número digitado foi {}, \nseu dobro é {}, \nseu triplo é {} \nsua raiz é {: .0f}'.format(n, do, tri, rz), ' \nrespectivamente !!!') 

    # Desenvolva um programa que laia a s duas notas de um aluno, calcule e mostre sua média 

    print('7- Desenvolva um programa que laia a s duas notas de um aluno, calcule e mostre sua média ')

    aluno2 = input('Digite o nome do aluno: ')
    nota_1 = int(input('Digite a nota_1: '))
    nota_2 = int(input('Digite a nota_2: '))
    soma = int(nota_1) + int(nota_2) 
    media = soma / 2
    # resposta do exercício 07
    print(' R- A media das notas do aluno {} é {}'.format(aluno2,media ))

    # Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

    print('7- Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.')

    v1 = int(input('Digite um valor em metros: '))
    cen = int(v1 * 10)
    mili = int(v1 * 1000)
    # resposta do exercício 07
    print(' R- O valor digitado foi {}m \nseu valor em centímetros é {}cm \nseu valor em milímetros é {}mm'.format(v1, cen, mili))

    iniciar = input('Deseja continuar? (sim/não): ')
    if iniciar.lower() != 'sim':
        break
    
