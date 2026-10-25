# -*- coding: utf-8 -*-
import os
import sys
def lerN1():
    n1 = float(input('Nota1: '))
    return n1

def lerN2():
    n2 = float(input('Nota2: '))
    return n2

def getMedia(n1, n2):
    media = (n1 + n2) / 2
    return media

def mostrar(media):
    os.system('clear')
    print(f'\nMédia = {media}')
    if media < 6:
        print('\nAluno Reprovado')
    else:
        print('\nAluno Aprovado')
    os.system('sleep 5')

def executar():
    nota1 = lerN1()
    nota2 = lerN2()
    media = getMedia(nota1, nota2)
    mostrar(media)

def menu():
    while True:
        os.system('clear')
        print('=== MENU - CÁLCULO DE MÉDIA ===')
        print('1. Calcular a média')
        print('2. Sair')
        
        opcao = int(input('Escolha uma opção: '))
        
        if opcao == 1:
            executar()
        elif opcao == 2:
            print('\nEncerrando o programa...')
            break
        else:
            print('\nOpção inválida! Pressione Enter para tentar novamente.')
            os.system('sleep 2')

menu()
sys.exit()