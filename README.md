# Documentação da API Aqua Metrics

## Introdução
Este projeto consiste em uma API desenvolvida para facilitar a leitura e adição de dados em um banco de dados MongoDB. Utilizando Python, FastAPI, Pydantic e Pymongo, a API permite operações de leitura (GET) e inserção (POST) de dados de forma simples e eficiente.

## Tecnologias Utilizadas
- **Python**: Linguagem de programação utilizada para desenvolver a API.
- **FastAPI**: Framework para a construção de APIs que facilita o uso de métodos HTTP.
- **Pydantic**: Biblioteca utilizada para validar dados e criar classes que representam os dados da API.
- **Pymongo**: Biblioteca para interação com o MongoDB.

## Estrutura do Projeto
- **server.py**: Contém a implementação da API e a lógica de conexão com o MongoDB.
- **requirements.txt**: Lista as dependências do projeto.
- **vercel.json**: Configurações para a implantação no Vercel.

## API Endpoints

### 1. `GET /documentos`
- **Descrição**: Retorna todos os documentos armazenados na coleção do MongoDB.
- **Funcionamento**: 
  - A função `ler_documentos` utiliza `collection.find` para buscar os documentos e os adiciona a uma lista.
  - Os documentos são retornados em formato de dicionário.
  
### 2. `POST /documentos`
- **Descrição**: Adiciona um novo documento à coleção do MongoDB.
- **Parâmetros**:
  - `data` (string): Data e hora do registro.
  - `ph` (string): Valor do pH.
  - `tds` (string): Total de sólidos dissolvidos.
  - `temp` (string): Temperatura.
- **Funcionamento**:
  - A função `inserir_documento` recebe os dados, cria um dicionário e insere o documento no banco usando `insert_one`.
  - Retorna uma mensagem de confirmação se a inserção for bem-sucedida.
### 3. `GET /documentos/ultimo`
- **Descrição**: Retorna todos o ultimo documento armazenados na coleção do MongoDB.
- **Funcionamento**: 
  - A função `lerUltimoDocumento` utiliza `collection.find_one` para buscar o ultimo documentos e o adiciona a uma variavel.
  - Os documentos são retornados em formato de um dicionario.

## Conexão com o MongoDB
A aplicação se conecta ao MongoDB usando as credenciais fornecidas e especifica o nome do banco de dados e a coleção correspondente. 
