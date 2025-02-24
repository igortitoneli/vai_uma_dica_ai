# Vai Uma Dica Ai API

## Execução
### Rodar API
1. Crie um arquivo chamado `.env` na pasta docker. Você pode usar arquivo
   `.env.example` como base.

2. Suba os containers com o comando:
```sh
$ docker compose up -d --build
```

### Comando pra reboot
```sh
$ docker compose down -v && docker compose up -d
```


## Arquitetura

### Router

O Router é responsável por definir as rotas da aplicação, mapeando as requisições HTTP para os controladores apropriados. Ele garante que cada endpoint seja associado à função correta no Controller.

### Controller

O Controller atua como intermediário entre as requisições do cliente e a lógica de negócios da aplicação. Ele recebe as requisições, chama os serviços necessários e retorna as respostas apropriadas.

### Service

O Service contém a lógica de negócios da aplicação. Ele é responsável por processar os dados, aplicar regras e chamar os repositórios para acessar o banco de dados, garantindo uma separação clara entre a lógica de negócios e a manipulação direta de dados.

### Repository

O Repository gerencia a comunicação com o banco de dados. Ele encapsula as operações de CRUD (Create, Read, Update, Delete) e fornece uma interface para o Service acessar os dados sem expor detalhes da implementação do banco de dados.

### Model

O Model representa a estrutura dos dados da aplicação. Ele define os esquemas das entidades, suas propriedades e relacionamentos, garantindo que os dados sejam armazenados e manipulados corretamente.


