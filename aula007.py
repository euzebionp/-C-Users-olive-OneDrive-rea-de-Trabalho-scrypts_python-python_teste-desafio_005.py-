#operadores aritiméticos
print('='*5, 'desafio 07', '='*5)

nome = input('Didite seu nome ')
cidade = input('Digite sua cidade: ')
idd = input('Digite sua idade: ')

print('Olá! {}, Sua idade é {} anos, Seja bem vido de {} !!!'.format(nome, idd, cidade))
print('='*5, ' Vamos calcular', '='*5)

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2 # soma
m = n1 * n2 # multiplicação
d = n1 / n2 # divisão
di = n1 // n2 # divisão inteira
e = n1 ** n2 # expoente
mo = n1 % n2 # módulo

print('A soma vale {}, O produto vale {} e a divisão vale {: .3f}'. format(s, m, d), end=',')
print('a divisão inteira vale {}, a potência vale {} e o modulo da divisão vale {} '.format(di, e, mo))






