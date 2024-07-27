# SpotNews

SpotNews é um aplicativo de notícias desenvolvido com Django que permite o cadastro e gerenciamento de notícias e categorias, proporcionando uma interface intuitiva para visualização de detalhes das notícias.

## Índice

- [Visão Geral](#visão-geral)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)

## Visão Geral

SpotNews é um projeto que visa facilitar a publicação e a gestão de notícias, permitindo que usuários autenticados criem, editem e visualizem notícias e suas respectivas categorias. O aplicativo oferece uma interface amigável e intuitiva, com recursos como upload de imagens e categorização de notícias.

## Tecnologias Utilizadas

- Python
- Django
- HTML/CSS
- JavaScript
- SQLite (ou outro banco de dados suportado pelo Django)
- Bootstrap (para estilização)

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

4. Aplique as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```

5. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

## Como Usar

Depois de instalar e iniciar o servidor, acesse o aplicativo no navegador através do endereço [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Funcionalidades

- **Cadastro de Notícias:** Acesse [http://127.0.0.1:8000/news-form](http://127.0.0.1:8000/news-form) para cadastrar uma nova notícia.
- **Visualização de Notícias:** Acesse [http://127.0.0.1:8000/](http://127.0.0.1:8000/) para visualizar todas as notícias cadastradas.
- **Gestão de Categorias:** Acesse [http://127.0.0.1:8000/category-form](http://127.0.0.1:8000/category-form) para cadastrar novas categorias.

## Contribuição

Para contribuir com o projeto:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature:
    ```bash
    git checkout -b minha-feature
    ```
3. Comite suas mudanças:
    ```bash
    git commit -m 'Adiciona minha feature'
    ```
4. Faça o push para a branch:
    ```bash
    git push origin minha-feature
    ```
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para entrar em contato, acesse meu perfil no [GitHub](https://github.com/seu-usuario) ou envie um e-mail para seu-email@example.com.
