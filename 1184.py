opcao =input()
matriz = []

for i in range(12):
    matriz.append([])
    for j in range(12):
        numero = float(input())
        matriz[i].append(numero)

if opcao == 'S':
    soma = 0
    indice = 11
    for i in range(11,0, -1):
        for j in range(0, indice):
            soma += matriz[i][j]
        indice -= 1
    print(f'{soma:.1f}')

if opcao == 'M':
    soma = 0
    indice = 11
    quant = 0
    for i in range(11,0,-1):
        for j in range(0, indice):
            soma += matriz[i][j]
            quant += 1
        indice -= 1
      
    media = soma / quant
    print(f'{media:.1f}')