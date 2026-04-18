# ✅ Gerenciador de Tarefas (To-Do List)
Projeto desenvolvido como parte do Checkpoint 2, com foco em boas práticas de programação, modularização e persistência de dados.

## 📌 Descrição
 Um sistema de gerenciamento de tarefas via terminal, com arquitetura modular e persistência em JSON.
Permite ao usuário adicionar, visualizar, concluir e remover tarefas de forma simples, mantendo os dados salvos mesmo após o encerramento do programa.

## 🚀 Funcionalidades

➕ Adicionar novas tarefas
📋 Listar todas as tarefas
✅ Marcar tarefas como concluídas
❌ Remover tarefas
💾 Persistência automática em arquivo (tarefas.json)
🏗️ Arquitetura do Projeto

O projeto foi estruturado utilizando modularização, separando responsabilidades:

## 🔧 tarefas.py — Motor Lógico
Responsável por:

Gerenciar a lista de tarefas
Adicionar novas tarefas
Marcar tarefas como concluídas
Remover tarefas
Salvar e carregar dados do arquivo JSON

## 🖥️ main.py — Interface do Usuário
Responsável por:

Exibir o menu interativo
Capturar entradas do usuário
Chamar as funções do módulo lógico

## 🧠 Estrutura de Dados
As tarefas são armazenadas como uma lista de dicionários no formato:

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

## 🧩 Etapas do Desenvolvimento

## 🔹 Fase 1: MVP (Produto Mínimo Viável)
Criação da lista de tarefas
Função para adicionar tarefas
Função para listar tarefas
Menu básico com opções:
Adicionar
Listar
Sair

## 🔹 Fase 2: Atualização
Exibição com índice e status:
[X] tarefa concluída
[ ] tarefa pendente
Implementação da função para concluir tarefas
Nova opção no menu para marcar tarefas

💡 Uso de try/except IndexError para evitar erros ao acessar índices inválidos.

## 🔹 Fase 3: Persistência de Dados
Utilização da biblioteca json
Salvamento automático em tarefas.json
Carregamento dos dados ao iniciar o sistema

## 📷 Exemplo de Uso
=== GERENCIADOR DE TAREFAS ===

1 - Adicionar tarefa
2 - Listar tarefas
3 - Concluir tarefa
4 - Remover tarefa
5 - Sair

## 💻 Como Executar
Clone ou baixe este repositório
Certifique-se de ter o Python instalado
Execute o arquivo principal:
python main.py

## 🛠️ Tecnologias Utilizadas
Python 3
JSON (persistência de dados)

##🚧 Melhorias Futuras
Interface gráfica (GUI)
Sistema de usuários
Filtro de tarefas (pendentes/concluídas)
Integração com banco de dados (SQLite ou PostgreSQL)
Versão web ou mobile

##🎯 Objetivo do Projeto
Consolidar conhecimentos em:

Estruturas de dados (listas e dicionários)
Funções e modularização
Tratamento de erros (try/except)
Manipulação de arquivos
Organização de projetos

##👨‍💻 Autor
Guilherme Bouvier
Projeto desenvolvido como atividade acadêmica (Checkpoint 2)
