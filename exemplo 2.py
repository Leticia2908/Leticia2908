# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:09:00 2024

@author: 202307566837
"""

print("Olá", "mundo", sep="-") # Saída: Olá-mundo
print("Olá", "Python", end="!\n") # Saída: Olá Python!

# Saída: 18/04/2023 (formato de data)
print("18", "04", "2023", sep="/")
# Saída: nome; sobrenome; email (útil em CSVs)
print("nome", "sobrenome", "email", sep="; ") 

print("Loading", end=" ")
print("[OK]") # Saída: Loading [OK] 

#nome = input("Digite seu nome: ")
#print("Olá", nome)


#itens = input("Digite itens separados por vírgula: ").split(',')
#print("Itens:", itens)

#idade = int(input("Digite sua idade: "))
#print("Daqui a cinco anos, você terá", idade + 5, "anos.")

#altura = float(input("Digite sua altura em metros: "))
#print("Sua altura é", altura, "metros.")

def trinta_por_cento():
    print("Digite números para adicionar à lista (digite 'done' para terminar):")
    numeros = []
    while True:
        entrada = input()
        if entrada.lower() == 'done':
            break
        else:
            numeros.append(int(entrada))
    print("Números coletados:", numeros)
    
    
    
    
trinta_por_cento


#def imprimir_informacoes(nome, idade, cidade):
    #print("Nome:", nome, end=' | ')
    #print("Idade:", idade, end=' | ')
    #print("Cidade:", cidade)

# Exemplo de uso da função
#imprimir_informacoes("João", 25, "São Paulo")


#def calcular():
    # Solicita os números e a operação ao usuário
    #num1 = float(input("Digite o primeiro número: "))
    #num2 = float(input("Digite o segundo número: "))
    #operacao = input("Digite a operação desejada (+, -, *, /): ")

    # Verifica a operação e calcula o resultado
   # if operacao == '+':
        #resultado = num1 + num2
    #elif operacao == '-':
       # resultado = num1 - num2
    #elif operacao == '*':
        #resultado = num1 * num2
    #elif operacao == '/':
        # Verifica se o segundo número é zero para evitar divisão por zero
       # if num2 != 0:
            #resultado = num1 / num2
        #else:
           # print("Erro: Divisão por zero!")
           # return

    # Imprime o resultado da operação
   # print("O resultado de {} {} {} é: {}".format(num1, operacao, num2, resultado))

# Exemplo de uso da função
#calcular()


#def lista_de_compras():
    # Solicita ao usuário para digitar os itens da lista de compras
    #entrada = input("Digite os itens da lista de compras, separados por vírgula: ")

    # Divide a entrada do usuário em uma lista de itens
    #itens = entrada.split(',')

    # Imprime os itens da lista de compras em linhas separadas
    #print("Lista de Compras:")
    #for item in itens:
        #print(item.strip())  # strip() remove espaços em branco extras

# Exemplo de uso da função
#lista_de_compras()


#def celsius_para_fahrenheit():
    # Solicita ao usuário a temperatura em Celsius
    #celsius = float(input("Digite a temperatura em graus Celsius: "))

    # Converte Celsius para Fahrenheit usando a fórmula: (Celsius * 9/5) + 32
    #fahrenheit = (celsius * 9/5) + 32

    # Imprime o resultado da conversão
    #print("A temperatura em Fahrenheit é:", fahrenheit)

# Exemplo de uso da função
#celsius_para_fahrenheit()

def digitar_nomes():
    nomes = []  # Inicializa uma lista vazia para armazenar os nomes
    
    # Loop para solicitar ao usuário que digite nomes
    while True:
        nome = input("Digite um nome (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break  # Sai do loop se 'sair' for digitado
        nomes.append(nome)  # Adiciona o nome à lista
    
    # Imprime todos os nomes digitados, cada um em uma linha
    print("Nomes digitados:")
    for nome in nomes:
        print(nome)

# Exemplo de uso da função
digitar_nomes()

