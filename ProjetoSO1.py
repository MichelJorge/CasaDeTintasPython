#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime


print("\t\v***CASA DE TINTAS TARGARYAN\v***")
print("\t**Rua dos Lírios 137 - Santa Isabel - SP**")
print("\t*Telefone: 11-4656-2520 - email: vendas@casadetintasdta.com.br*\n\n")

print("ORÇAMENTO DE PINTURA")
print("Verifque o rendimento de cada tipo de tinta de acordo com o fabricante\n")
print("As latas de tintas possuem 18 litros.\n")


cliente = str ( input ('Nome do Cliente: \n'))

tamanho = int(input('Tamanho da Área  a ser pintada em metros quadrados: \n')) # tamanho da área a ser pintada

rendimento = float (input('Rendimento por metro quadrado: \n'))   # rendimento por metro quadrado

litros = tamanho / rendimento                                   # quantidade de tinta em litros                                  

valor = float (input('Valor de cada lata em Reais: \n'))  # valor da lata de um litro de tinta



if tamanho % 54 == 0:                           # verifica a quantidade de latas , retornando o sempre um valor inteiro
	latas = tamanho / 54
else: 
	latas = int(tamanho / 54) + 1

preco = latas * valor                           # imprime quantidade de latas e o valor total dos produtos
print ('%d latas fechadas' %latas)
print ('Valor Total: R$ %.2f' %preco)

sim = int (input ('\nAperte: 1 = IMPRESSÃO ou <ENTER> para Sair\n'))

if sim :
        print ("\n\n\n\n\n\n\n\nORÇAMENTO CASA DE TINTAS TARGARYAN\n")
        print ("Orçamento válido por 4 dias\n")
        print (cliente)
        print ('%d Latas' %latas)
        print ('Valor Total ----> R$ %.2f' % preco)
        now = datetime.now()
        print (now)

        
else:
        print ("FIM DO PROGRAMA")

input ("\n\t\tAperte <ENTER> para Sair")



