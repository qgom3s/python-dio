# Segundo Desafio - Python

> Intruções do desafio proposto e descrição da solução apresentada.

O desafio consiste em melhorar o desafio anterior - "banco" que possui as operações de saque, depósito e extrato - modularizando o código através do uso de funções com algumas condições de contorno definidas e utilizando recursos do Python apresentados no módulo de estrutura de dados.

## Descrição do Desafio

**Objetivo geral**: Separar as funcionalidades existentes - depósito, saque e extrado - em funções e criar duas novas funcionalidades - cadastrar usuário (client) e cadastrar conta bancária.

Para exercitar os conceitos deste módulo, cada função terá pelo menos uma regra de passagem de argumentos. O retorno e a forma como serão chamadas é livre.

Funcionalidades:
- _Depósito_: além das condições definidas no primeiro desafio, a função depósito deve receber os argumentos apenas por posição (_positional only_).
    - sugestão de argumentos: saldo, valor, extrato.
    - sugestão de retornos: saldo e extrato.
- _Saque_: além das condições definidas no primeiro desafio, a função saque deve receber o argumento apenas por nome (_keyword only_).
    - sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.
    - sugestão de retornos: saldo e extrato.
- _Extrato_: além das condições definidas no primeiro desafio, a função extrato deve receber os argumentos por posição e nome (_positional only_ e _keyword only_).
    - argumento posicional: saldo.
    - argumento nomeado: extrato.
- _Adicionar Usuário_: o programa deve armazenar usuários em uma lista - e composto por nome, data de nascimento, cpf e endereço. Deve ser armazenado somente o número do cpf, não podendo cadastrar mais de um usuário com o mesmo cpf.
    - o endereço é uma `string` com o formato: logradouro, número, bairo, cidade, sigla do estado.
- _Criar nova Conta_: o programa deve armazenar contas em uma lista que será composta por: agência, número da conta e usuário.
    - o número da conta deve ser sequêncial e começando em 1.
    - o número da agência é fixo: "0001".
    - o usuário pode ter mais de uma conta, porém uma conta pertence somente a um usuário.

_Dica do Instrutor_: Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.

Além das duas novas funções obrigatórias, o uso de mais funções visando melhorar ou implementar outras funcionalidades é encorajado.

## Requisitos - Fundamentos de Python

Conceitos abordados de Python que são essenciais para a resolução do desafio proposto:

- Listas;
- Tuplas;
- Conjuntos;
- Dicionários;
- Métodos característicos de cada estrutura anterior e,
- Funções em Python.

## Resolução Proposta

A solução desenvolvida pode ser observada no arquivo `bank_v2.py` e aplicação de conceitos como: estrutura de dados, funções e encapsulamento - embora não tenha sido muito abordada até esta etapa do curso.

Para as funcionalidades que realizam operações, foram criados funções apropriadas conforme as condições passadas e toda a parte em que o usuário realiza uma simulação de ações foi colocada dentro da função `operations()`. Portanto, todas as funcionalidades herdadas do desafio 01 estão modularizadas.

Como não existe inteção de usar conceitos de orientação a objetos e muito menos carregar dados de contas e usuários no momento, optei por somente criar as funções que resolvem a atividade proposta e um laço condicional para que seja possível testar tanto as funcionalidades de gerenciamento de usuários e contas, encapsuladas em `user_management()`, como as de operações de um usuário com conta "ativa". Isso irá deixar o código simples, com os recursos abordados até o momento do curso, além de já estar pronto para implementar classes e objetos.
