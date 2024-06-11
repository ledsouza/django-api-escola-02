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
        Verifica se uma requisição GET para a URL de listagem de cursos retorna o status HTTP 200 OK,
        indicando que a lista de cursos foi obtida com sucesso.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_curso(self):
        """
        Testa a criação de um novo curso através de uma requisição POST.

        Valida se:

        * O status code da resposta é HTTP 201 CREATED, indicando que o curso foi criado.
        * Os dados do curso criado (código, descrição, nível) estão corretos na resposta.
        """
        novo_curso = {
            'id': 3,
            'codigo_curso': 'CTT3',
            'descricao': 'Curso teste 3',
            'nivel': 'I'
        }
        response = self.client.post(self.list_url, data=novo_curso)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertDictEqual(response.data, novo_curso)
