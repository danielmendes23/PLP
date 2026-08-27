# Atividade Prática - Interoperabilidade com Jython

Este repositório contém a entrega da atividade focada na exploração do **Jython**, demonstrando a capacidade de interoperabilidade entre as linguagens Python e Java na mesma plataforma de execução.

## Sobre o Jython
Jython é uma implementação da linguagem Python desenvolvida para executar diretamente sobre a Máquina Virtual Java (JVM). Ele compila o código-fonte Python para *bytecode* Java de forma transparente, o que possibilita aos desenvolvedores importar, instanciar e utilizar classes, métodos e bibliotecas do ecossistema Java de maneira nativa, utilizando a sintaxe limpa e expressiva do Python.

## Programas Desenvolvidos

Os exemplos escolhidos focam em operações de terminal (CLI), utilizando entrada e saída padrão para interagir com o usuário, e foram pensados para refletir componentes comuns no dia a dia do desenvolvimento:

1. **Exemplo 1 (`exemplo1.py`) - Módulo de Gestão de Despesas:**
   Um utilitário de terminal para cadastrar e calcular gastos essenciais (como aluguel, água e feira). O script é voltado para auxiliar na organização das finanças da moradia, agrupando as categorias e somando o total gasto utilizando o poder das estruturas de dados do Java sob uma lógica Python.

2. **Exemplo 2 (`exemplo2.py`) - Analisador de Latência do Sistema:**
   Um simulador que avalia paralelamente o tempo de resposta de dois serviços críticos (Banco de Dados e API Externa). As latências geradas nos testes ficam estimadas entre 180 ms e 300 ms, permitindo observar o comportamento de múltiplas tarefas executando ao mesmo tempo (multithreading) dentro da JVM.

## Classes e Bibliotecas Java Utilizadas
Ao longo dos dois scripts, o projeto fez uso direto do pacote `java.lang` e `java.util`:
* `java.util.Scanner`: Para capturar dinamicamente os inputs de texto digitados pelo usuário no console.
* `java.lang.System`: Utilizado especificamente com o atributo `System.in` para fornecer o fluxo de entrada padrão ao `Scanner`.
* `java.util.ArrayList`: Estrutura de lista dinâmica utilizada para armazenar as despesas individuais.
* `java.util.HashMap`: Dicionário/Mapa utilizado para organizar os arrays de despesas por chave de categoria (ex: "Moradia", "Alimentação").
* `java.lang.Thread`: Classe fundamental do Java para criação e gerenciamento das threads na execução paralela de latência.
* `java.lang.Runnable`: Interface Java implementada para definir a tarefa que a thread irá executar em paralelo.
* `java.lang.InterruptedException`: Exceção tratada no caso de interrupção forçada dos testes durante as chamadas de `.sleep()`.

## A Integração Python-Java

A interoperabilidade entre os dois ecossistemas se torna evidente de algumas formas cruciais nestes exemplos:
* **Importação Direta:** O código Python importa as classes Java como se fossem módulos comuns (ex: `from java.util import HashMap`).
* **Sintaxe Híbrida:** No `exemplo1.py`, após popular as coleções Java (`ArrayList` e `HashMap`), iteramos sobre elas utilizando o tradicional laço `for in` do Python (`for valor in valores:`), demonstrando que o Jython traduz perfeitamente as iterações e tipos de dados.
* **Herança Transparente:** No `exemplo2.py`, criamos uma classe puramente Python (`class VerificadorLatencia`) que herda e implementa os requisitos de uma **interface Java** (`Runnable`). O objeto Python é então instanciado e repassado para o construtor da classe nativa `java.lang.Thread`, permitindo que o ambiente Java gerencie a execução concorrente ditada por código Python.

---

## Como Executar o Projeto

### 1. Executando Localmente (Sem Docker)
Você precisará do Java e do arquivo standalone do Jython.

1. Baixe o `jython-standalone-2.7.4.jar` (ou versão equivalente) e coloque-o na raiz deste diretório.
2. Abra seu terminal na pasta do projeto.
3. Para rodar o **Exemplo 1**, execute o comando:
   ```bash
   java -Dfile.encoding=UTF-8 --enable-native-access=ALL-UNNAMED -jar jython-standalone-2.7.4.jar exemplo1.py
   ```
4. Para rodar o **Exemplo 2**, execute o comando:
   ```bash
   java -Dfile.encoding=UTF-8 --enable-native-access=ALL-UNNAMED -jar jython-standalone-2.7.4.jar exemplo2.py
   ```

> *Nota: As flags `-Dfile.encoding` evitam quebras de acentuação no terminal, e a flag `--enable-native-access` suprime avisos de segurança nas versões mais recentes da JVM.*

### 2. Executando via Docker
Caso possua o Docker instalado, você não precisará baixar o `.jar` do Jython, o próprio contêiner cuidará disso. Como o projeto é interativo (requer digitação pelo terminal), usaremos a flag `-it`.

1. Faça o build da imagem do projeto usando o Dockerfile incluso:
   ```bash
   docker build -t atividade-jython .
   ```
2. Execute o contêiner de forma interativa, escolhendo qual script deseja rodar (ex: `exemplo1.py`):
   ```bash
   docker run -it --rm atividade-jython exemplo1.py
   ```
3. Para rodar o segundo script, basta trocar o nome do arquivo:
   ```bash
   docker run -it --rm atividade-jython exemplo2.py
   ```
