# Terceiro Desafio - Python

> Intruções do desafio proposto e descrição da solução apresentada.

O desafio consiste em melhorar o desafio anterior - "banco" que possui as operações de saque, depósito e extrato - modelando o código através do uso de programação orientada a objetos com algumas condições de contorno definidas e utilizando recursos do Python apresentados no módulo de OOP.

## Descrição do Desafio

**Objetivo geral**: Iniciar a modelagem do sistema bancário utilizando OOP, adicionar classes para clientes e operações bancárias: depósito e saque, atualizar o sistema bancário para armazenar dados de clientes e contas bancárias em objetos ao invés de dicionários.

Para exercitar os conceitos deste módulo, cada classe e método deverar seguir as condições especificadas no UML apresentado em funcionalidades.

Funcionalidades:

![alt text](uml.png)

Além das duas novas features obrigatórias, fica como desafio extra, modelar por OOP os métodos que tratam as opções do menu fazendo com que trabalhem com as classes modeladas.

## Requisitos - Fundamentos de Python

Conceitos abordados de Python que são essenciais para a resolução do desafio proposto:

- Fundamentos de Python;
- Estrutura de dados;
- Conceitos de Programação Orientada a Objetos;
- Herança utilizando Python;
- Encapsulamento em Python;
- Polimorfismo em Python,
- Interfaces e Classes Abstratas em Python.

## Resolução Proposta

A solução proposta apresenta as seguintes características:

1. **Classes:**
   - **Person:** Representa um indivíduo com atributos como nome, data de nascimento, CPF e endereço.
   - **Account:** Representa uma conta bancária com atributos como número da conta, agência, saldo e cliente.
   - **CheckingAccount:** Herda de `Account` e representa uma conta corrente com atributos adicionais como limite de saque e limite de transação.
   - **History:** Armazena detalhes das transações, como tipo, valor e data/hora.`.
   - **Client:** Representa um cliente com atributos como endereço e uma lista de contas.

2. **Métodos:**
   - **Client:** Contém métodos para realizar transações (`perform_transaction`) e adicionar contas (`add_account`).
   - **Account:** Contém métodos para depositar (`deposit`) e sacar (`withdraw`) dinheiro.
   - **CheckingAccount:** Sobrescreve o método `withdraw` para aplicar limites de saque.
   - **History:** Armazena e recupera o histórico de transações.
   - **Transactions:** Define métodos abstratos para registrar transações.

3. **Uso:**
   - Os clientes podem criar contas e realizar transações, como depósitos e saques.
   - As contas mantêm o histórico de transações e aplicam limites de saque para contas correntes.

No geral, a solução fornece uma abordagem estruturada e orientada a objetos para modelar um sistema bancário básico, permitindo o gerenciamento fácil de clientes, contas e transações.
