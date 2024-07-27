# SpotNews

SpotNews é um aplicativo de notícias desenvolvido com Django que permite o cadastro e gerenciamento de notícias e categorias, proporcionando uma interface intuitiva para visualização de detalhes das notícias.

## Índice

- [Visão Geral](#visão-geral)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Licença](#licença)
- [Contato](#contato)

## Visão Geral

SpotNews é um projeto que visa facilitar a publicação e a gestão de notícias, permitindo que usuários autenticados criem, editem e visualizem notícias e suas respectivas categorias. O aplicativo oferece uma interface amigável e intuitiva, com recursos como upload de imagens e categorização de notícias.

## Tecnologias Utilizadas

- Python
- Django
- HTML/CSS
- MySQL
- Docker

## Instalação

Para instalar o SpotNews localmente, siga os passos abaixo:

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/spotnews.git
    cd spotnews
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Construa a imagem Docker para o banco de dados:
    ```bash
    docker build -t spotnews-db .
    ```

5. Execute o contêiner Docker para o banco de dados:
    ```bash
    docker run -d -p 3306:3306 --name=spotnews-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=spotnews_database spotnews-db
    ``` 

6. Aplique as migrações do banco de dados:
    ```bash
    python3 manage.py migrate
    ```

7. Execute o script de seeds:
   ```bash
    python3 manage.py runscript seeds
    ```

8. Inicie o servidor de desenvolvimento:
    ```bash
    python3 manage.py runserver
    ```

## Como Usar

Depois de instalar e iniciar o servidor, acesse o aplicativo no navegador através do endereço [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Funcionalidades

- **Visualização de Notícias:** Acesse [http://127.0.0.1:8000/](http://127.0.0.1:8000/) para visualizar todas as notícias cadastradas.
- **Cadastro de Notícias:** Acesse [http://127.0.0.1:8000/news](http://127.0.0.1:8000/news) para cadastrar uma nova notícia.
- **Gestão de Categorias:** Acesse [http://127.0.0.1:8000/categories](http://127.0.0.1:8000/categories) para cadastrar novas categorias.
- **API de Categorias:** Acesse [http://127.0.0.1:8000/api/categories](http://127.0.0.1:8000/api/categories) para visualizar a API de categorias.
- **API de Usuários:** Acesse [http://127.0.0.1:8000/api/users](http://127.0.0.1:8000/api/users) para visualizar a API de usuários.
- **API de Notícias:** Acesse [http://127.0.0.1:8000/api/news](http://127.0.0.1:8000/api/news) para visualizar a API de notícias.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para entrar em contato, acesse meu perfil no [GitHub](https://github.com/matheusrosa1) ou envie um e-mail para seu-email@example.com.
