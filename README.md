
# MiniTwitter

MiniTwitter é uma aplicação Django que permite criar posts, seguir perfis e interagir com outros usuários. Este projeto inclui uma API documentada com Swagger e utiliza PostgreSQL como banco de dados.

## Pré-requisitos

- [Docker](https://www.docker.com/get-started) instalado e em execução
- [Docker Compose](https://docs.docker.com/compose/install/) instalado

## Configuração do Ambiente

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/minitwitter.git
   cd minitwitter
   ```

2. **Configure o arquivo `.env`:**

   Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis de ambiente:

   ```env
   # Django
   DJANGO_SECRET_KEY=sua-chave-secreta
   DJANGO_DEBUG=True

   # Banco de Dados
   DB_NAME=postgres
   DB_USER=postgres
   DB_PASSWORD=sua-senha
   DB_HOST=db
   DB_PORT=5432
   ```

## Rodando o Projeto com Docker

### 1. Build e Iniciar os Containers

Na raiz do projeto, execute o seguinte comando para construir e rodar os containers:

```bash
docker-compose up --build
```

Isso irá:
- Baixar a imagem base do Python e PostgreSQL, se necessário.
- Instalar as dependências do Python.
- Rodar o servidor Django na porta `8000`.
- Rodar o banco de dados PostgreSQL no container `db`.

### 2. Aplicar Migrações e Rodar aplicação localmente

Depois que os containers estiverem em execução, abra um novo terminal e execute:

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```


### 3. Acessar a Aplicação

- A aplicação estará disponível em: [http://localhost:8000](http://localhost:8000)
- A documentação da API estará disponível em: [http://localhost:8000/](http://localhost:8000/) (Swagger UI)
- A documentação Redoc estará em: [http://localhost:8000/redoc](http://localhost:8000/redoc)
- O painel de administração do Django estará em: [http://localhost:8000/admin](http://localhost:8000/admin)

## Comandos Úteis

### Parar os Containers

Para parar os containers sem removê-los, use:

```bash
docker-compose stop
```

### Reiniciar os Containers

Para reiniciar os containers:

```bash
docker-compose start
```

### Remover Todos os Containers, Volumes e Imagens Criados

```bash
docker-compose down -v
```

### Executar Comandos dentro do Container Web

Se precisar executar qualquer comando dentro do container web (por exemplo, para rodar novas migrações ou criar superusers), você pode usar:

```bash
docker-compose exec web python manage.py <comando>
```

## Estrutura de Pastas do Projeto

```
minitwitter/
│
├── core/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── signals.py
│   └── ...
│
├── minitwitter/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── .env
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── manage.py
```

## Notas Adicionais

- Certifique-se de que o Docker Desktop está em execução antes de tentar iniciar o projeto.
- Todas as variáveis de ambiente devem ser definidas no arquivo `.env` para garantir que o projeto funcione corretamente no Docker.
- Os containers `web` e `db` são definidos no arquivo `docker-compose.yml`, que gerencia toda a configuração e dependências.


## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## DER e Diagrama de classes

![Diagrama DER](/assets/img/minitwitter-der.png)
![Diagrama de classes](/assets/img/minitwitter-arc.png)
