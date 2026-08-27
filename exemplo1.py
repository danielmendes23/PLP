# -*- coding: utf-8 -*-
from java.util import Scanner, ArrayList, HashMap
from java.lang import System

print(u"--- Módulo de Gestão de Despesas ---")

scanner = Scanner(System.in)
financas = HashMap()

despesas_moradia = ArrayList()
print(u"Digite o valor do Aluguel (ex: 1200.50): ")
aluguel_str = scanner.nextLine()
despesas_moradia.add(float(aluguel_str))

print(u"Digite o valor da Conta de Água: ")
agua_str = scanner.nextLine()
despesas_moradia.add(float(agua_str))

despesas_alimentacao = ArrayList()
print("Digite o valor gasto na Feira da semana: ")
feira_str = scanner.nextLine()
despesas_alimentacao.add(float(feira_str))

financas.put("Moradia", despesas_moradia)
financas.put(u"Alimentação", despesas_alimentacao)

total_geral = 0.0

print(u"\n--- Resumo das Despesas ---")
for categoria in financas.keySet():
    valores = financas.get(categoria)
    subtotal = 0.0

    for valor in valores:
        subtotal += valor

    print("Categoria: " + categoria + " | Subtotal: R$ " + str(subtotal))
    total_geral += subtotal

print("------------------------------------")
print("Despesa Total Registrada: R$ " + str(total_geral))
