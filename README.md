## API da Escola - Django REST Framework com Cache e Tradução

![Static Badge](https://img.shields.io/badge/Status-Finalizado-green)

## Descrição

Este projeto implementa uma API REST completa para gerenciar dados de uma escola fictícia, desenvolvida durante o curso de Django REST Framework da Alura. A API fornece acesso a informações sobre alunos, cursos e matrículas, além de implementar recursos avançados como cache com Redis e tradução personalizada. O projeto é uma continuação do projeto [api-escola](https://github.com/ledsouza/api-escola), expandindo suas funcionalidades e boas práticas.

<img width="1181" alt="image" src="https://github.com/ledsouza/django-api-escola-testes/assets/56280624/0548204a-cbdf-4d71-a8e7-1d8d74e4bf7c">

## Tecnologias Utilizadas

- Python 3
- Django
- Django REST Framework
- Redis
- APITestCase (Django REST Framework)

## Funcionalidades Detalhadas

**Recursos:**

- **Alunos:** Consultar, adicionar, editar e informações de alunos.
- **Cursos:** Consultar, adicionar, editar e remover informações de cursos.
- **Matrículas:** Consultar, adicionar e editar matrículas de alunos em cursos.

**Funcionalidades Adicionais:**

- **Cache com Redis:** Implementação de cache para otimizar o desempenho da API, armazenando dados em cache no Redis.
- **Tradução Personalizada:** Tradução da API utilizando arquivos `.po` para oferecer suporte a múltiplos idiomas.
- **Testes Unitários:** Cobertura de testes unitários utilizando APITestCase do Django REST Framework para garantir a qualidade e o funcionamento correto da API.

**Estrutura do Projeto:**

O projeto segue a estrutura padrão de um projeto Django, com os seguintes componentes principais:

- `models.py`: Define os modelos de dados da aplicação (Alunos, Cursos, Matrículas).
- `serializers.py`: Define os serializers para representar os modelos de dados em formato JSON.
- `views.py`: Define as views da API, que processam as requisições HTTP e retornam as respostas apropriadas.
- `urls.py`: Define as URLs da API, mapeando-as para as views correspondentes.
- `tests/`: Contém os testes unitários da API.
- `locale/`: Contém os arquivos `.po` para tradução da API.

## Como Executar o Projeto

1. Clone este repositório: `git clone https://github.com/seu_usuario/django-api-escola-02.git`
2. Inicialize o poetry: `poetry init`
3. Instale as dependências do projeto: `poetry install`
4. Ative o ambiente virtual: `poetry shell`
5. Aplique as migrações do banco de dados: 
    - `python manage.py makemigrations`
    - `python manage.py migrate`
6. Inicie o servidor de desenvolvimento: `python manage.py runserver`

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.
