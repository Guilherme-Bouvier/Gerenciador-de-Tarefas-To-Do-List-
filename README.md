# ✅ Gerenciador de Tarefas (To-Do List)
Projeto desenvolvido como parte do Checkpoint 2, com foco em boas práticas de programação, modularização e persistência de dados.

## 📌 Descrição
 Um sistema de gerenciamento de tarefas via terminal, com arquitetura modular e persistência em JSON.
Permite ao usuário adicionar, visualizar, concluir e remover tarefas de forma simples, mantendo os dados salvos mesmo após o encerramento do programa.

## 🚀 Funcionalidades<br>

➕ Adicionar novas tarefas <br>
📋 Listar todas as tarefas<br>
✅ Marcar tarefas como concluídas<br>
❌ Remover tarefas<br>
💾 Persistência automática em arquivo (tarefas.json)<br>
🏗️ Arquitetura do Projeto<br>

O projeto foi estruturado utilizando modularização, separando responsabilidades:

## 🔧 tarefas.py — Motor Lógico<br>
Responsável por:<br>

Gerenciar a lista de tarefas<br>
Adicionar novas tarefas<br>
Marcar tarefas como concluídas<br>
Remover tarefas<br>
Salvar e carregar dados do arquivo JSON<br>

## 🖥️ main.py — Interface do Usuário<br>
Responsável por:<br>

Exibir o menu interativo<br>
Capturar entradas do usuário<br>
Chamar as funções do módulo lógico<br>

## 🧠 Estrutura de Dados<br>
As tarefas são armazenadas como uma lista de dicionários no formato:<br>

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

## 🧩 Etapas do Desenvolvimento<br>

## 🔹 Fase 1: MVP (Produto Mínimo Viável)<br>
Criação da lista de tarefas<br>
Função para adicionar tarefas<br>
Função para listar tarefas<br>
Menu básico com opções:<br>
Adicionar<br>
Listar<br>
Sair<br>

## 🔹 Fase 2: Atualização<br>
Exibição com índice e status:<br>
[X] tarefa concluída<br>
[ ] tarefa pendente<br>
Implementação da função para concluir tarefas<br>
Nova opção no menu para marcar tarefas<br>

💡 Uso de try/except IndexError para evitar erros ao acessar índices inválidos.<br>

## 🔹 Fase 3: Persistência de Dados<br>
Utilização da biblioteca json<br>
Salvamento automático em tarefas.json<br>
Carregamento dos dados ao iniciar o sistema<br>

## 📷 Exemplo de Uso<br>
=== GERENCIADOR DE TAREFAS ===<br>

1 - Adicionar tarefa<br>
2 - Listar tarefas<br>
3 - Concluir tarefa<br>
4 - Remover tarefa<br>
5 - Sair<br>

## 💻 Como Executar<br>
Clone ou baixe este repositório<br>
Certifique-se de ter o Python instalado<br>
Execute o arquivo principal:<br>
python main.py<br>

## 🛠️ Tecnologias Utilizadas<br>
Python 3<br>
JSON (persistência de dados)<br>

## 🚧 Melhorias Futuras<br>
Interface gráfica (GUI)<br>
Sistema de usuários<br>
Filtro de tarefas (pendentes/concluídas)<br>
Integração com banco de dados (SQLite ou PostgreSQL)<br>
Versão web ou mobile<br>

## 🎯 Objetivo do Projeto<br>
Consolidar conhecimentos em:<br>

Estruturas de dados (listas e dicionários)<br>
Funções e modularização<br>
Tratamento de erros (try/except)<br>
Manipulação de arquivos<br>
Organização de projetos<br>

## 👨‍💻 Autor<br>
Guilherme Bouvier<br>
Projeto desenvolvido como atividade acadêmica (Checkpoint 2)<br>
