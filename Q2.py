# -*- coding: utf-8 -*-
import os
import time

comprimento = 0.0
diametro = 0.0
raio = 0.0
area = 0.0
pi = 3.14
opcao = 0

dados_lidos = False
calculo_feito = False

while True:
    os.system('clear')
    print("===== MENU DE CÁLCULO DO CÍRCULO =====")
    print("1 - Leitura do Comprimento")
    print("2 - Cálculo (Diâmetro, Raio e Área)")
    print("3 - Impressão dos Resultados")
    print("4 - Saída\n")

    try:
        opcao = int(input("Digite uma opção: "))
    except ValueError:
        print("\nPor favor, digite apenas números inteiros!")
        time.sleep(1.5)
        continue

    if opcao == 1:
        os.system('clear')
        print("--- 1. LEITURA ---\n")
        comprimento = float(input("Digite o comprimento do círculo: "))
        
        dados_lidos = True
        calculo_feito = False
        print("\nComprimento lido com sucesso!")
        time.sleep(1.5)

    elif opcao == 2:
        os.system('clear')
        print("--- 2. CÁLCULO ---\n")
        
        if not dados_lidos:
            print("Erro: Faça a Leitura (Opção 1) antes de calcular!")
        else:
            diametro = comprimento / pi
            raio = diametro / 2
            area = pi * (raio ** 2)
            calculo_feito = True
            print("Cálculos realizados com sucesso!")

        time.sleep(1.5)

    elif opcao == 3:
        os.system('clear')
        print("--- 3. IMPRESSÃO DOS RESULTADOS ---\n")
        
        if not calculo_feito:
            print("Erro: Faça o Cálculo (Opção 2) antes de imprimir!")
        else:
            print(f"Diâmetro = {diametro:.2f}")
            print(f"Raio = {raio:.2f}")
            print(f"Área = {area:.2f}")

        print("\n----------------------------------")
        input("Pressione Enter para voltar ao menu...")

    elif opcao == 4:
        print("\nSaindo do programa...")
        break

    else:
        print("\nOpção inválida! Escolha entre 1 e 4.")
        time.sleep(1.5)