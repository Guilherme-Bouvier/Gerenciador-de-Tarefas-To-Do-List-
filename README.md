# ✅ Gerenciador de Tarefas (To-Do List)

Projeto desenvolvido como parte do Checkpoint 2, com foco em boas práticas de organização de código, modularização e persistência de dados.

## 📌 Descrição

Este projeto consiste em um sistema simples de gerenciamento de tarefas via terminal. O usuário pode adicionar, listar e marcar tarefas como concluídas, com salvamento automático em arquivo para manter os dados mesmo após o encerramento do programa.

## 🚀 Funcionalidades

O sistema permite:

➕ Adicionar novas tarefas
📋 Listar todas as tarefas salvas
✅ Marcar tarefas como concluídas
💾 Salvar os dados automaticamente (persistência em JSON)
🏗️ Arquitetura do Projeto

O projeto foi estruturado utilizando modularização, separando responsabilidades em diferentes arquivos:

## 📁 projeto/
│
├── tarefas.py   # Motor lógico (regras de negócio)
├── main.py      # Interface com o usuário (menu interativo)
└── dados.json   # Armazenamento das tarefas

## 🔧 tarefas.py — Motor Lógico

Responsável por:

Gerenciar a lista de tarefas
Adicionar novas tarefas
Marcar tarefas como concluídas
Salvar e carregar dados do arquivo JSON

## 🖥️ main.py — Painel do Usuário

Responsável por:

Exibir o menu interativo
Capturar entradas do usuário
Chamar as funções do módulo lógico

## 🧠 Estrutura de Dados

As tarefas são armazenadas como uma lista de dicionários, no seguinte formato:

[
    {
        "descricao": "estudar python",
        "concluida": true
    },
    {
        "descricao": "pagar a luz",
        "concluida": false
    }
]


# 🧩 Etapas do Desenvolvimento

## 🔹 Fase 1: MVP (Produto Mínimo Viável)
Criação da lista de tarefas
Função para adicionar tarefas
Função para listar tarefas
Menu básico com opções:
Adicionar
Listar
Sair

## 🔹 Fase 2: Atualização (Update)
Exibição com índice e status:
[X] tarefa concluída
[ ] tarefa pendente
Implementação da função para concluir tarefas
Nova opção no menu para marcar tarefas

💡 Dica: uso de try/except IndexError para evitar erros ao acessar índices inválidos.

## 🔹 Fase 3: Persistência de Dados
Uso da biblioteca json
Salvamento automático em dados.json
Carregamento dos dados ao iniciar o sistema


## 💻 Como Executar
Clone ou baixe o projeto
Certifique-se de ter o Python instalado
Execute o arquivo principal:
python main.py

## 🛠️ Tecnologias Utilizadas
Python 3
JSON (para persistência de dados)

## 🎯 Objetivo do Projeto

Este projeto tem como objetivo consolidar conhecimentos em:

Estruturas de dados (listas e dicionários)
Funções e modularização
Tratamento de erros (try/except)
Manipulação de arquivos
Organização de projetos

## 👨‍💻 Autor
Guilherme Bouvier
Desenvolvido como atividade acadêmica (Checkpoint 2).
