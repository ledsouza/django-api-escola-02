from rest_framework.test import APITestCase
from rest_framework import status
from escola.models import Curso
from django.urls import reverse


class CursoTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT1',
            descricao='Curso teste 1',
            nivel='B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso='CTT2',
            descricao='Curso teste 2',
            nivel='A'
        )

    def test_requisicao_get_para_listar_cursos(self):
        """
        Verifica se uma requisição GET para a URL de cursos retorna o status HTTP 200 OK,
        indicando que a lista de cursos foi obtida com sucesso.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_curso(self):
        """
        Verifica se uma requisição POST para a criação de um novo curso retorna HTTP 201
        CREATED, indicando que o curso foi criado.
        """
        novo_curso = {
            'id': 3,
            'codigo_curso': 'CTT3',
            'descricao': 'Curso teste 3',
            'nivel': 'I'
        }
        response = self.client.post(self.list_url, data=novo_curso)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_curso(self):
        """
        Verifica se uma requisição DELETE para deletar um curso retorna o status HTTP 405 METHOD NOT ALLOWED,
        indicando que o método DELETE não é permitido para esta URL.

        Este teste garante que a API não permita a exclusão de cursos através de requisições DELETE.
        """
        response = self.client.delete(self.list_url + '1/')
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_requisicao_put_para_atualizar_curso(self):
        """
        Verifica se uma requisição PUT para atualizar um curso retorna o status HTTP 200 OK,
        indicando que o curso foi atualizado com sucesso.

        Este teste garante que a API permita a atualização de cursos através de requisições PUT,
        enviando os dados atualizados no corpo da requisição.
        """
        curso_atualizado = {
            'codigo_curso': 'CTT1',
            'descricao': 'Curso teste 1 atualizado',
            'nivel': 'I'
        }
        response = self.client.put(self.list_url + '1/', data=curso_atualizado)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
