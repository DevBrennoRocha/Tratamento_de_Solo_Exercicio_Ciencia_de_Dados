import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time, sys
import numpy as np

#Amostras de dados:

# Amostra de solo 1
amostra1 = {
    "local": "A",
    "ph": 6.5,
    "nitrogenio": 10.2,
    "fosforo": 4.8,
    "potassio": 2.3
}

# Amostra de solo 2
amostra2 = {
    "local": "B",
    "ph": 7.2,
    "nitrogenio": 8.5,
    "fosforo": 3.2,
    "potassio": 2.8
}

# Amostra de solo 3
amostra3 = {
    "local": "C",
    "ph": 5.8,
    "nitrogenio": 12.1,
    "fosforo": 5.6,
    "potassio": 1.9
}

# Lista que contém as amostras de solo
amostras_de_solo = [amostra1, amostra2, amostra3]

amostras = [
    {"local": "Área A", "ph": 6.8, "nitrogenio": 0.2,
        "fosforo": 0.15, "potassio": 0.3},

    {"local": "Área B", "ph": 5.9, "nitrogenio": 0.35,
        "fosforo": 0.12, "potassio": 0.25},
]

#analise de dados
#Calcule a média do pH, nitrogênio, fósforo e potássio para todas as amostras.

#Identifique as amostras com níveis de pH abaixo de 6.5 e mostre essas informações.

# analise de dados2

ph_total = 0
nitrogenio_total = 0
potassio_total = 0
fosforo_total = 0
ph_baixo_6_5 = []

count = len(amostras)

    #LOOPING de avalores totais
for amostra in amostras:
    ph_total += amostra["ph"]
    nitrogenio_total += amostra["nitrogenio"]
    fosforo_total += amostra["fosforo"]
    potassio_total += amostra["potassio"]

# Filtragem De amostras de PH
    if amostra['ph']<6.5:
        ph_baixo_6_5.append(amostra)

ph_media = ph_total / count
nitrogenio_media = nitrogenio_total / count
fosforo_media = fosforo_total / count
potassio_media = potassio_total/count

#Menu: "Agro-Menu"

def task ():
    for x in range(1000):
        print('X')
        time.sleep(0.002)

    print('fim')
    time.sleep(2)


def menu():
    print()
    print("Aperte |c| para ver comandos: ")
    command = input('comandos: ')

    match command:
        case '':
            print()
            print('Digite um comando: ')
        case 'c':
            print('--------------------------------')
            print("Agro Menu:")
            print("|1| Media Do PH de Nitrogenio.")
            print("|2| Media Do PH de Fosforo.")
            print("|3| Media Do PH de Potassio.")
            print("|4| proximo ->")
            print('---------------------------------')
        case '1':
            print(f"Média de Nitrogênio: {nitrogenio_media:.2f}")
        case '2':
            print(f"Média de Fósforo: {fosforo_media:.2f}")
        case '3':
            print(f"Média de Potássio: {potassio_media:.2f}")
        case '4':
            print('---------------------------------------------------')
            print('|5| Recomendações de plantio.')
            print('|6| Recomendação Nitrogenio Baixo.')
            print('|7|identificação de mostras a baixo de 6.5 no PH.')
            print('|8|Salvar como relatorio.')
            print('-------------------------------------------------')
        case '5':
            if ph_media <6.0:
                print("Recomendção: Aplicar Calagem para ajustar o PH do solo!")
            else:
              print("Não necessita de Recomendação")
        case '6':
            if nitrogenio_media >0.3:
                print("Recomendação: Aplicar Fertilizantes Controlados Ricos em Hidrogênio")
            else:
              print("Não precisa de recomendação")
        case '7':
            if ph_baixo_6_5:
                  print("Amostras De PH A baixo de |6.5|:")
            for amostra in ph_baixo_6_5:
                  print(f"local: {amostra['local']}, PH: {amostra['ph']}")
            else:
                print("Não ha Amostras Com niveis de PH baixo de 6.5")
        case '8':
              salvar = input("Deseja salvar um relatório? (s/n)").lower() == 's'
              if (salvar == 's'):
                    with open("relatorio_solo.txt", "w") as arquivo:
                        arquivo.write("Relatório de Solo\n\n")
                        arquivo.write(f"Média de Nitrogênio: {nitrogenio_media:.2f}\n")
                        arquivo.write(f"Média de Fósforo: {fosforo_media:.2f}\n")
                        arquivo.write(f"Média de Potássio: {potassio_media:.2f}\n\n")
                        arquivo.write("Amostras com níveis de pH abaixo de 6.5:\n")
                        if ph_baixo_6_5:
                            for amostra in ph_baixo_6_5:
                                arquivo.write(f"Local: {amostra['local']}, pH: {amostra['ph']}\n")
                        else:
                            arquivo.write("Não há amostras com níveis de pH abaixo de 6.5\n")
                    print("Relatório salvo com sucesso!")

print("---Tratamento_de_solo (ver.alfa.01)---")

while True:
    print()
    menu()
    
    #Geração de graficos
    
df = pd.DataFrame(amostras_de_solo)

# Propriedades do solo (categorias)
cat = ['ph', 'nitrogenio', 'fosforo', 'potassio']

# Criar o gráfico
plt.figure(figsize=(25, 6))
for i in range(len(cat)):
    plt.subplot(1, 4, i + 1)
    sns.countplot(data=df, x=cat[i], hue='local', palette='Set3')
    plt.title(f'Contagem de {cat[i]} por Local', fontsize=14)
    plt.tight_layout()

plt.show()