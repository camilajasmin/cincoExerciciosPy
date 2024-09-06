"""
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor 
sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci 
e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""

# INÍCIO
print('Digite um número e descubra se ele pertence à sequência de Fibonacci!')
print(70*'-')
# VARIÁVEIS
n = 100000
t1 = 1
t2 = 0
t3 = 0
t4 = []

# CÁCULO DA SEQUÊNCIA PARA VERIFICAÇÃO
while t1 <= n:
    t4.append(t1)
    t3 = t1 + t2
    t2 = t1
    t1 = t3

while True:
    try:
        num = int(input('Digite aqui o número desejado para verificação: '))
        if num in t4:
            print(f'Sim, o número {num} está na sequência de Fibonacci.')
        else:
            print(f'O número {num} não pertence à sequência de Fibonacci')
        break
    except:
        print('Preencha com um inteiro, por favor.')
        continue
