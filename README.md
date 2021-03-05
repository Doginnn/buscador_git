# buscador_git - [Em Desenevolvimento]

Um simples buscador na API do GitHub que retorna as informações e repositórios mais populares de uma empresa parceira.

## Dependências

- [Python](https://www.python.org/downloads/) - Versão 3.8
- [django](http://www.djangoproject.com) - 3.1

## Instalação:
1. Clone o projeto
    ```bash
    git clone https://github.com/Doginnn/buscador_git.git
    ```

2. Instalar e ativar Pipenv ([Pypa](https://pypi.org/project/pipenv/))

3. Instalar todas as dependências do Pipenv necessárias para a API rodar:

    ```bash
    pipenv install
    ```

4. Sincronize a base de dados com os comandos 4 e 5:

    ```bash
    python manage.py makemigrations
    ```
5. Sincronize a base de dados:
   
   ```bash
    python manage.py migrate
   ```
   
6. Crie um usuário (Administrador do sistema): Nesse caso o meu Usuário ADM é `"teste"` e Senha ADM é `"123Teste!"`, não esqueça de configurar esse usuário e senha lá em `settings.py`>>`DATABASES`.

    ```bash
    python manage.py createsuperuser
    ```

7. Teste a instalação carregando o servidor de desenvolvimento (http://127.0.0.1:8000/ no navegador):

    ```bash
    python manage.py runserver
    ```

## Créditos

- [Diógenes Dantas](https://github.com/Doginnn)

## Ajuda

Para relatar bugs, fazer perguntas ou até mesmo contribuir utilize o [Issues](https://github.com/Doginnn/buscador_git/issues) ou via email diogenesemmanuel@gmail.com
