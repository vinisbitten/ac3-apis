# AC3 Desenvolvimento de APIs - API de Registros

## Pré-requisitos

- Python 3.7
- Pip
- Docker

## Instalação

0. Instale as dependências do projeto

```bash
pip install flask &&\
pip install psycopg2-binary
```

1. Clone o repositório

```bash
git clone https://github.com/vinisbitten/ac3-apis.git
```

2 - Acesse a pasta docker do projeto

```bash
cd ac3-apis/docker
```

3 - Execute o comando para criar a imagem do banco de dados

```bash
docker build -t ac3-db .
```

4 - Execute o comando para criar o container do banco de dados

```bash
docker run -d -p 5432:5432 ac3-db
```

5 - Acesse a pasta raiz do projeto e inicialize as rotas


```bash
cd .. &&\
python app.py
```

## Rotas

As rotas disponíveis são:

- GET /registros
- POST /registros
- DELETE /registros/{id}

Utilize o arquivo `AC3.json` para importar as rotas no Postman.