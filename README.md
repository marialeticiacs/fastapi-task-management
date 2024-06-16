# Sistema de Gerenciamento de Tarefas

## Objetivo
Este projeto tem como objetivo desenvolver um sistema de gerenciamento de tarefas para a disciplina de Programação Multiplataforma 1. Utilizando o framework FastAPI, o projeto aplica conceitos de controllers, services e repositories.

## Descrição do Projeto
O projeto consiste em uma API para gerenciamento de tarefas, permitindo a criação, leitura, atualização e exclusão de tarefas. Cada tarefa possui um título, descrição, status e data de criação.

## Estrutura do Projeto
Estrutura de diretórios:

```plaintext
fastapi-task-management/
├── app/
│   ├── controllers/
│   │   └── task_controller.py
│   ├── services/
│   │   └── task_service.py
│   ├── repositories/
│   │   └── task_repository.py
│   ├── models/
│   │   ├── task_model.py
│   │   └── task_schema.py
│   ├── main.py
│   └── database.py
└── requirements.txt
```



