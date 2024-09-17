'''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''
print('Invertendo os caracteres de uma string!')
print(40*'-')

string = input('Digite seu nome: ')
tamanhoString = len(string)
i = 0


print(f'A string é "{string}" e seu tamanho é de {tamanhoString} caracteres incluindo os espaços')

while i > -tamanhoString:
    i-=1
    char = string[i]
    print(char)