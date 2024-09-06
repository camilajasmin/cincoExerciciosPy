'''
Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o 
percentual de representação que cada estado teve dentro do valor 
total mensal da distribuidora.
'''
print('Vamos lá!')
print(50*'-')


'''
SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
OUTROS = 19849.53
for i in TUDO:
   total +=i
'''
TUDO = [67836.43, 36678.66 , 29229.88, 27165.48, 19849.53]
total = 0
for i in TUDO:
   total +=i


print(f'Uma distribuidora obteve o total de R${total} de faturamento mensal')
es= input('Estes são os estados onde a transportadora atua, informe o estado e direi a porcentagem que ele representa do total de faturamento SP, RJ, MG, ES ou OUTROS:')
estado = es.upper()
porcentagem=0
if estado == 'SP':
    estado = TUDO[0]
    porcentagem = (estado/total) * 100
elif estado == 'RJ':
    estado = TUDO[1]
    porcentagem = (estado/total) * 100
elif estado == 'MG':
    estado = TUDO[2]
    porcentagem = (estado/total) * 100
elif estado == 'ES':
    estado = TUDO[3]
    porcentagem = (estado/total) * 100
elif estado == 'OUTROS':
    estado = TUDO[4]
    porcentagem = (estado/total) * 100
else:
    print('Não existe essa opção.')

print (f'Este estado representa {porcentagem:.2f}% to faturamento total mensal.')