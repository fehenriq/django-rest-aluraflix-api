# Formulário com Django

Provedor local de séries e filmes com Django REST API

## 🔨 Funcionalidades do projeto

Registrar programas [titulo, tipo, data_lancamento, likes]  
Filtros de campo e pesquisa  
Autenticação básica implementada  
Métodos permitidos autenticado: GET, POST, PUT e DELETE  
Quando não autenticado: GET e POST  
Documentado com Swagger e Redoc

## ✔️ Técnicas e tecnologias utilizadas

- `Python`
- `Django`
- `Django REST Framework`
- `Swagger`

## 🛠️ Abrir e rodar o projeto

Para abrir e rodar o projeto, execute os comandos:
- python -m venv venv
- venv/scripts/activate
- pip install -r requirements.txt
- py manage.py makemigrations
- py manage.py migrate
- py manage.py createsuperuser
- py manage.py runserver
