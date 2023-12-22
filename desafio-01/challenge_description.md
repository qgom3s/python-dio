# Primeiro Desafio - Python

> Intruções do desafio proposto e descrição da solução apresentada.

O desafio consiste em criar um "banco" e simular as operações de saque, depósito e extrato, com algumas condições de contorno e utilizando recursos do Python apresentados no módulo de fundamentos da linguagem.

## Descrição do Desafio

**Objetivo geral**: Criar um sistema bancário com as operações de saque, depósito e visualização do extrato.

Funcionalidades:
- _Depósito_: deve ser possível depositar valores positivos para a conta bancária. A versão 1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
- _Saque_: O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
- _Extrato_: Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações. Os valores devem ser exibidos utilizando o formato **R$ xxx.xx**.

## Requisitos - Fundamentos de Python

Conceitos abordados de Python que são essenciais para a resolução do desafio proposto:

- Review da Linguagem - História e informações relevantes;
- Configuração do ambiente para desenvolvimento;
- Tipos de dados;
- Tipos de operadores;
- Estruturas condicionais;
- Estruturas de repetição e,
- Strings e manipulação de strings.

## Resolução Proposta

A solução desenvolvida pode ser observada no arquivo `bank_v1.py` e aplicação de conceitos como: condicionais, repetição usando `while`, uso de contador, strings, variáveis e uso de aninhamento para modelar as condições de contorno para a funcionalidade de saque.
