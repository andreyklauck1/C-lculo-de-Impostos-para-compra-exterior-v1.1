import requests

url = 'https://open.er-api.com/v6/latest/BRL'

req = requests.get(url)

dados = req.json()

def calculoInt(produto, frete, moeda):
    total = produto + frete
    total = total / dados['rates'][moeda]
    print(f'\nTotal convertido em BRL: \nR${round(total, 2) } \n')
    if total >= 250:
        impImportacao = total * 0.60
        print(f'Imposto de Importação (60%): \nR${round(impImportacao, 2)} \n')
        total = total + impImportacao
        print(f'Total incluindo Imposto de Importação (60%): \nR${round(total, 2)} \n')
    icms = total * (18/100)
    print(f'ICMS (18%): \nR${round(icms, 2)} \n')
    total = total + icms
    print(f'Total: \nR${round(total, 2)}')
    
produto = float(input('Escreva o valor do produto: '))
frete = float(input('Escreva o valor do frete: '))
moeda = input(f'Escreva a moeda do produto: ').upper()
calculoInt(produto, frete, moeda)