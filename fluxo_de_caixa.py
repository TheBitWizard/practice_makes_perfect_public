'''
Script rápido para praticar linguagem Python 3.

Esse script simula um fluxo de caixa, apresentando um
menu ao usuário, requisitando entradad de informações,
e exibindo a lista de transacoes conforme forem
adicionadas.

Foram adicionados recursos de validação de entrada de 
para previnir erros não tratados e manter a 
continuidade do programa.

Foi criada uma base com mensagens padrão para garantir
a compreensão da lógica do código enquanto são 
exibidas mensagens mais robustas que oferecem melhor
legibilidade ao utilizar o programa.
'''

import os
import time
import math

erros = {
    "invalido":"O valor digitado não é válido",

    "opcao":"A opção selecionada não está listada acima. Selecione novamente."
}

mensagens = {
    "titulo_principal":'''
===============================
Fluxo de caixa
-------------------------------''',

    "menu_principal":'''
1- Adicionar receita
2- Adicionar despesa
0- Finalizar fluxo
-------------------------------''',

    "receita_titulo":'''
===============================
Receita''',

    "despesa_titulo":
    '''
===============================
Despesa''',

    "entrada_data":'''-------------------------------
Data (dd/mm/aa): ''',

    "entrada_desc":'''-------------------------------
Descrição: ''',

    "entrada_valor":'''-------------------------------
Valor R$: '''
}


# Lista para conter cada transacao do fluxo de caixa em formato de dicionário.
fluxo_de_caixa = []




def exibir_transacoes():
    if len(fluxo_de_caixa) > 0:
        for fc in fluxo_de_caixa:
            print(f'''
{fc["data"]}
-------------------------------
{fc["descricao"]}\t\t\t{fc["valor"]}''')
            





            
def adicionar_transacao(transacao):
    # A entrada 'transacao' é recebida como um texto
    # e validada abaixo. Caso seja numéria, será
    # convertida para um inteiro. Se a entrada não for
    # numerica, o programa irá informar o usuário para
    # tentar novamente, explicitando o motivo.
    if transacao.isnumeric():
        transacao = int(transacao)

        if transacao == 0:  # Opção Finalizar fluxo
            return 0 # Romper o loop
        
        elif transacao == 1:  # Opção Receita
            print(mensagens["receita_titulo"])

            tipo = "receita" # O dado 'tipo' é importante para permitir a soma de todas as transacoes por categoria.
            data = str(input(mensagens["entrada_data"]))
            descricao = input(mensagens["entrada_desc"])
            valor = float(input(mensagens["entrada_valor"]))
            valor = math.sqrt(math.pow(valor, 2)) # Força o valor a ser sempre positivo.
            fluxo_de_caixa.append({"tipo": tipo, "data": data, "descricao":descricao, "valor":valor})

            return -1   # Fluxo normal do programa. Segue sem romper o loop.

        elif transacao == 2: # Opção Despesa
            print(mensagens["despesa_titulo"])

            tipo = "despesa" # O dado 'tipo' é importante para permitir a soma de todas as transacoes por categoria.
            data = str(input(mensagens["entrada_data"]))
            descricao = input(mensagens["entrada_desc"])
            valor = float(input(mensagens["entrada_valor"]))
            valor = 0-math.sqrt(math.pow(valor, 2)) # Força o valor a ser sempre negativo.
            fluxo_de_caixa.append({"tipo": tipo, "data": data, "descricao":descricao, "valor":valor})

            return -1   # Fluxo normal do programa. Segue sem romper o loop.

        # Caso o usuário insira um charactere numérico
        # porém não incluso na lista de opções, será
        # exibida um aviso pedindo que o usuário tente
        # novamente, explicitando o motivo.
        else:
            return 1
    else:
        # Caso o usuário insira um charactere não 
        # numérico porém não incluso na lista de 
        # opções, será exibida um aviso pedindo que
        # o usuário tente novamente, explicitando o 
        # motivo.
        return 2





# Retorna a soma total de todas as transacoes do fluxo de caixa.
def somar_transacoes(transacao):
    transacao = transacao.lower() # Garante que os caracteres estejam todos em minusculo, assim como o padrao do dicionario.

    soma = 0
    for fc in fluxo_de_caixa:
        if fc["tipo"] == transacao:
            soma += fc["valor"]
    return soma

    


# Execução do do programa.
while True:
    os.system("cls")

    print(mensagens["titulo_principal"])

    exibir_transacoes()

    print(mensagens["menu_principal"])
    
    transacao = input("Digite uma das opções acima: ")

    if adicionar_transacao(transacao) == -1: # Fluxo normal do loop.
        continue

    if adicionar_transacao(transacao) == 0: # Finaliza o programa
        break

    elif adicionar_transacao(transacao) == 1: # Valor digitado não é uma opção da lista.
        print(erros["opcao"])
        time.sleep(4)

    elif adicionar_transacao(transacao) == 2: # Valor digitado não é um número
        print(erros["invalido"])
        time.sleep(2)

receita = somar_transacoes("Receita")
despesa = somar_transacoes("Despesa")
saldo = receita+despesa

print(f'''
===========================
Receita total:\t{receita}
Despesa total:\t{despesa}
Saldo:\t\t{saldo}
===========================''')