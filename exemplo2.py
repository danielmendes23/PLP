# -*- coding: utf-8 -*-
import random
from java.lang import Thread, Runnable, InterruptedException, System
from java.util import Scanner

print(u"--- Analisador de Latência do Sistema ---")

scanner = Scanner(System.in)
print(u"Digite a quantidade de testes de ping (iterações) por serviço: ")
iteracoes_str = scanner.nextLine()
quantidade_iteracoes = int(iteracoes_str)

class VerificadorLatencia(Runnable):
    def __init__(self, nome_servico, iteracoes):
        self.nome_servico = nome_servico
        self.iteracoes = iteracoes

    def run(self):
        print("Iniciando monitoramento: " + self.nome_servico)

        for i in range(1, self.iteracoes + 1):
            latencia = random.randint(180, 300)
            print("[" + self.nome_servico + "] Ping " + str(i) + ": " + str(latencia) + " ms")

            try:
                Thread.sleep(500)
            except InterruptedException:
                print("A thread " + self.nome_servico + " foi interrompida.")

        print(u">>> Concluído: " + self.nome_servico)

tarefa_banco = VerificadorLatencia("Banco de Dados", quantidade_iteracoes)
tarefa_api = VerificadorLatencia("API Externa", quantidade_iteracoes)

thread1 = Thread(tarefa_banco)
thread2 = Thread(tarefa_api)

print("\nIniciando testes paralelos...\n")
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("------------------------------------")
print(u"Análise finalizada com sucesso.")