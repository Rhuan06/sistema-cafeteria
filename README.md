<div align="center">

# ☕ Sistema de Gestão para Cafeteria

### Sistema Full Stack de Ponto de Venda (PDV)

Desenvolvido com **FastAPI**, **PostgreSQL** e **JavaScript**

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />

<br>

Projeto desenvolvido para simular um sistema comercial moderno de gerenciamento de produtos e vendas, aplicando conceitos de **Arquitetura REST**, **POO**, **Clean Code**, **Persistência Relacional** e **Desenvolvimento Full Stack**.

</div>



---

## ✨ Funcionalidades

### 📦 Gestão de Produtos

✔ Cadastro de produtos

✔ Listagem dinâmica

✔ Validação contra duplicidade

✔ Exclusão lógica (Soft Delete)

✔ Persistência em PostgreSQL

---

### 🧾 Ponto de Venda (PDV)

✔ Carrinho inteligente

✔ Controle de quantidade de itens

✔ Cálculo automático de totais

✔ Finalização de pedidos

✔ Interface responsiva

✔ Feedback visual com modais e notificações

---

### 🔒 Integridade dos Dados

✔ Transações ACID

✔ Chaves estrangeiras

✔ Validação de dados

✔ Tratamento de erros

✔ Separação de responsabilidades

---

## 🏗️ Arquitetura

```text
Frontend (HTML + CSS + JavaScript)
               │
               ▼
       FastAPI REST API
               │
               ▼
      PostgreSQL Database
```

---

## 🛠️ Stack Tecnológica

| Categoria      | Tecnologias                  |
| -------------- | ---------------------------- |
| Backend        | Python, FastAPI, Pydantic    |
| Banco de Dados | PostgreSQL, psycopg2         |
| Frontend       | HTML5, CSS3, JavaScript      |
| Ferramentas    | Git, GitHub, Uvicorn, Dotenv |

---

## 📁 Estrutura do Projeto

```text
sistema_cafeteria/
│
├── backend/
│   ├── controllers/
│   ├── database/
│   ├── models/
│   ├── api.py
│   └── .env
│
└── frontend/
    ├── index.html
    ├── style.css
    └── app.js
```

---

## 🚀 Executando o Projeto

### Clone o repositório

```bash
git clone https://github.com/seu-usuario/sistema-cafeteria.git
```

### Crie e ative o ambiente virtual

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux/Mac

```bash
source .venv/bin/activate
```

### Instale as dependências

```bash
pip install -r backend/requirements.txt
```

### Configure o arquivo .env

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=sistema_cafeteria
DB_USER=postgres
DB_PASSWORD=sua_senha
```

### Execute a API

```bash
python -m backend.database.setup_db

uvicorn backend.api:app --reload
```

### Swagger

```text
http://127.0.0.1:8000/docs
```

---

## 🎯 Conceitos Aplicados

* Programação Orientada a Objetos (POO)
* API REST
* Clean Code
* Arquitetura em Camadas
* Soft Delete
* Transações ACID
* Integração Front-end ↔ Back-end
* Consumo de APIs com Fetch
* Persistência Relacional

---

## 📈 Roadmap

* [x] CRUD de Produtos
* [x] CRUD de Pedidos
* [x] PostgreSQL
* [x] API REST
* [x] Interface Web
* [x] Soft Delete
* [ ] Controle de Estoque
* [ ] Dashboard Administrativo
* [ ] Relatórios Financeiros
* [ ] Autenticação de Usuários
* [ ] Deploy em Nuvem

---

## 👨‍💻 Autor

### Rhuan

Desenvolvedor em formação com foco em:

* Python
* FastAPI
* PostgreSQL
* JavaScript
* Desenvolvimento Full Stack
* Arquitetura de Software
* Clean Code

---

<div align="center">

### ⭐ Se gostou do projeto, deixe uma estrela no repositório!

</div>
