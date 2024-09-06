"""
Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?
"""
# variáveis
INDICE = 13
SOMA = 0
K = 0

# observe o tipo da variável INDICE
print(f'INDICE é do tipo {type(INDICE)}')

while K < INDICE:
    K = K + 1; SOMA = SOMA + K
    print(f'até agora SOMA é igual a {SOMA} e agora K é igual a {K}')

# resultado
print(50*'-')
print(f'o valor final de "SOMA" é {SOMA}')
print(50*'-')