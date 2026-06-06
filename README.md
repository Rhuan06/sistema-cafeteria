# ☕ Sistema de Gestão para Cafeteria

![Python](https://img.shields.io/badge/Python-3.14+-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)

> Sistema de gerenciamento de produtos e pedidos desenvolvido em **Python** com persistência de dados em **PostgreSQL**.

Este projeto foi criado com foco em **Programação Orientada a Objetos (POO)**, **Clean Code**, **Arquitetura em Camadas** e **boas práticas de desenvolvimento Back-end**, simulando um cenário real de controle de estoque e registro de vendas para uma cafeteria.

---

## 📋 Sobre o Projeto

O sistema permite o gerenciamento completo de produtos e pedidos através de uma interface de linha de comando (CLI).

Além das operações de CRUD, o projeto implementa conceitos importantes de desenvolvimento de software, como:

* Encapsulamento com `@property` e `@setter`
* Persistência de dados em banco relacional
* Transações ACID
* Integridade referencial
* Separação de responsabilidades
* Variáveis de ambiente para proteção de credenciais

---

## 🚀 Funcionalidades

### 📦 Gestão de Produtos

✔ Cadastro de produtos

✔ Listagem do cardápio

✔ Atualização de preços

✔ Exclusão de produtos

✔ Validação de regras de negócio

---

### 🧾 Gestão de Pedidos

✔ Criação de pedidos com múltiplos itens

✔ Cálculo automático do valor total

✔ Histórico de vendas

✔ Exclusão de pedidos

✔ Relacionamento entre pedidos e produtos

---

### 🔒 Integridade dos Dados

✔ Transações ACID utilizando `commit()` e `rollback()`

✔ Relacionamentos com chaves estrangeiras

✔ Utilização de `ON DELETE CASCADE`

✔ Validação de dados antes da persistência

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia    | Finalidade                   |
| ------------- | ---------------------------- |
| Python 3.10+  | Linguagem principal          |
| PostgreSQL    | Banco de dados relacional    |
| psycopg2      | Comunicação com o PostgreSQL |
| python-dotenv | Variáveis de ambiente        |
| Git           | Controle de versão           |
| GitHub        | Hospedagem do projeto        |

---

## 🧠 Conceitos Demonstrados

### Programação Orientada a Objetos

* Classes e Objetos
* Encapsulamento
* Properties e Setters
* Métodos Especiais (`__str__`)
* Type Hints

### Banco de Dados

* CRUD Completo
* Chaves Primárias
* Chaves Estrangeiras
* Relacionamentos
* Integridade Referencial
* Transações ACID

### Boas Práticas

* Clean Code
* Arquitetura em Camadas
* Separação de Responsabilidades
* Organização Modular
* Variáveis de Ambiente

---

## 📁 Estrutura do Projeto

```text
sistema_cafeteria/
│
├── controllers/
│   ├── pedido_controller.py
│   └── produto_controller.py
│
├── database/
│   ├── conexao.py
│   ├── queries.py
│   └── setup_db.py
│
├── models/
│   ├── produto.py
│   ├── item_pedido.py
│   └── pedido.py
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── main.py
```

### Organização das Camadas

| Pasta       | Responsabilidade                |
| ----------- | ------------------------------- |
| models      | Entidades e regras de negócio   |
| controllers | Operações e lógica da aplicação |
| database    | Conexão e consultas SQL         |
| main.py     | Interface CLI e fluxo principal |

---

## ⚙️ Instalação

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/sistema-cafeteria.git
cd sistema-cafeteria
```

---

### 2️⃣ Criar o ambiente virtual

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Linux / Mac

```bash
python -m venv .venv
source .venv/bin/activate
```

---

### 3️⃣ Instalar as dependências

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configurar o banco de dados

Crie um arquivo `.env` na raiz do projeto:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=sistema_cafeteria
DB_USER=postgres
DB_PASSWORD=sua_senha
```

---

### 5️⃣ Criar as tabelas

```bash
python -m database.setup_db
```

---

### 6️⃣ Executar a aplicação

```bash
python main.py
```

---

## 🔄 Exemplo de Transação

Ao finalizar um pedido o sistema executa:

1. Inserção do pedido
2. Recuperação do ID gerado
3. Inserção dos itens do pedido
4. Confirmação da transação

```python
try:
    conexao.commit()
except Exception:
    conexao.rollback()
```

Caso qualquer erro ocorra durante o processo, todas as alterações são revertidas automaticamente, garantindo a consistência dos dados.

---

## 🎯 Destaques Técnicos

* Integração Python + PostgreSQL
* Uso de Transações ACID
* Relacionamentos entre tabelas
* CRUD completo
* Arquitetura em Camadas
* Encapsulamento e Validação de Dados
* Uso de Type Hints
* Gerenciamento seguro de credenciais com `.env`

---

## 🚧 Roadmap

- [x] CRUD de produtos
- [x] CRUD de pedidos
- [x] Integração com PostgreSQL
- [x] Transações ACID
- [ ] Interface gráfica
- [ ] API REST
- [ ] Autenticação de usuários

## 👨‍💻 Autor

Desenvolvido por **Rhuan** como projeto de estudos para aprofundamento em:

* Python
* PostgreSQL
* Programação Orientada a Objetos
* Desenvolvimento Back-end
* Boas práticas de arquitetura de software


