# ☕ Sistema de Gestão para Cafeteria

Sistema de gerenciamento de produtos e pedidos desenvolvido em **Python** com persistência de dados em **PostgreSQL**.

O projeto foi construído com foco em **Programação Orientada a Objetos (POO)**, **Clean Code**, **Arquitetura em Camadas** e boas práticas de desenvolvimento back-end, simulando cenários reais de controle de estoque e registro de vendas.

---

## 🚀 Funcionalidades

### 📦 Gestão de Produtos

* Cadastro de produtos com validação de regras de negócio.
* Listagem completa do estoque.
* Atualização de preços.
* Exclusão de produtos.
* Validação para impedir preços negativos.

### 🧾 Gestão de Pedidos

* Criação de pedidos contendo múltiplos produtos.
* Associação entre pedidos e itens através de relacionamento relacional.
* Cálculo automático do valor total do pedido.
* Consulta do histórico de vendas.
* Cancelamento de pedidos.

### 🔒 Integridade dos Dados

* Utilização de **transações ACID** para garantir consistência.
* Uso de `commit()` para confirmação das operações.
* Uso de `rollback()` para desfazer alterações em caso de falha.
* Utilização de `ON DELETE CASCADE` para remoção automática dos itens vinculados a um pedido cancelado.

---

## 🛠️ Tecnologias Utilizadas

* Python 3.10+
* PostgreSQL
* psycopg2
* python-dotenv
* Git e GitHub

---

## 🧠 Conceitos Aplicados

### Programação Orientada a Objetos (POO)

* Encapsulamento com `@property` e `@setter`
* Classes e Objetos
* Métodos Especiais (`__str__`)
* Validação de dados dentro das entidades

### Banco de Dados Relacional

* Chaves Primárias
* Chaves Estrangeiras
* Relacionamentos 1:N
* Integridade Referencial
* Transações

### Boas Práticas

* Clean Code
* Type Hints
* Separação de Responsabilidades
* Arquitetura em Camadas
* Variáveis de Ambiente para credenciais

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
│   ├── pedido.py
│   ├── item_pedido.py
│   └── produto.py
│
├── .env
├── .gitignore
├── requirements.txt
└── main.py
```

### Estrutura em Camadas

| Camada      | Responsabilidade                            |
| ----------- | ------------------------------------------- |
| Models      | Regras de negócio e entidades               |
| Controllers | Operações e lógica da aplicação             |
| Database    | Conexão, criação de tabelas e consultas SQL |
| Main        | Interface CLI e fluxo do sistema            |

---

## ⚙️ Configuração do Ambiente

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/sistema-cafeteria.git
cd sistema-cafeteria
```

### 2. Criar e ativar o ambiente virtual

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/Mac**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuração do Banco de Dados

Crie um arquivo `.env` na raiz do projeto:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=sua_base_de_dados
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
```

---

## 🗄️ Criando as Tabelas

Execute:

```bash
python -m database.setup_db
```

---

## ▶️ Executando o Sistema

```bash
python main.py
```

---

## 🔄 Exemplo de Fluxo de Transação

Ao criar um pedido, o sistema:

1. Insere o pedido na tabela `pedidos`.
2. Recupera o ID gerado.
3. Insere os itens na tabela `itens_pedido`.
4. Confirma a operação com `commit()`.

Caso qualquer etapa falhe:

```python
conexao.rollback()
```

todas as alterações são desfeitas automaticamente, garantindo a consistência dos dados.

---

## 📚 Aprendizados Demonstrados

Este projeto demonstra conhecimentos em:

* Python para desenvolvimento back-end.
* PostgreSQL e modelagem relacional.
* Programação Orientada a Objetos.
* Manipulação de transações.
* Arquitetura em camadas.
* Integração Python + Banco de Dados.
* Boas práticas de desenvolvimento.

---

## 👨‍💻 Autor

Desenvolvido como projeto de estudos para aprofundamento em Python, Banco de Dados Relacionais e Desenvolvimento Back-end.
