# Título do Seu Projeto

Descrição breve do seu projeto.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados na sua máquina:

- Python 3.x
- Django
- SQLite

## Configuração

1. Clone o repositório:

git clone https://github.com/FelipeCecconello/projetopesquisa

2. Navegue até o diretório do projeto:

cd nome-do-repositorio

3. Crie um ambiente virtual (opcional):

python -m venv venv

4. Ative o ambiente virtual (opcional):

Windows
venv\Scripts\activate

macOS/Linux
source venv/bin/activate

5. Instale as dependências:

pip install -r requirements.txt

csharp
Copy code

6. Execute as migrações do banco de dados:

python manage.py migrate

7. Crie um superusuário (opcional):

python manage.py createsuperuser

8. Inicie o servidor de desenvolvimento:

python manage.py runserver

9. Acesse a aplicação no seu navegador em http://localhost:8000.

## Uso

- Faça login no Django Admin com as credenciais do superusuário criado.
- Crie professores, alunos, projetos de pesquisa e execute outras ações através do Django Admin.

## Contribuição

Se você quiser contribuir para este projeto, siga as etapas abaixo:

1. Faça um fork do repositório.
2. Crie uma nova branch: `git checkout -b minha-nova-feature`
3. Faça o commit das suas alterações: `git commit -m 'Adicionar nova feature'`
4. Faça o push para a branch criada: `git push origin minha-nova-feature`
5. Abra um Pull Request.
