from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Aluno, Curso, Matricula


class MatriculaTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Matriculas-list')
        self.detail_url = reverse('Matriculas-detail', args=[1])

        self.aluno_1 = Aluno.objects.create(
            nome='João da Silva',
            rg='123456789',
            cpf='12345678901',
            data_nascimento='2000-01-01',
            celular='11999999999'
        )

        self.curso_1 = Curso.objects.create(
            codigo_curso='INF01',
            descricao='Ciência da Computação',
            nivel='G',
        )

        self.matricula_1 = Matricula.objects.create(
            aluno=self.aluno_1,
            curso=self.curso_1,
            periodo='M'
        )

    def test_requisicao_get_para_listar_matriculas(self):
        """
        Verifica se uma requisição GET para a URL de matrículas retorna o status HTTP 200 OK,
        indicando que a lista de matrículas foi obtida com sucesso.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_matricula(self):
        """
        Verifica se uma requisição POST para a criação de uma nova matrícula retorna HTTP 201
        CREATED, indicando que a matrícula foi criada.
        """
        nova_matricula = {
            'aluno': self.aluno_1.id,
            'curso': self.curso_1.id,
            'periodo': 'V'
        }
        response = self.client.post(self.list_url, data=nova_matricula)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_get_para_detalhar_matricula(self):
        """
        Verifica se uma requisição GET para detalhar uma matrícula retorna o status HTTP 200 OK
        e os dados da matrícula correta.
        """
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['aluno'], self.matricula_1.aluno.id)
        self.assertEqual(response.data['curso'], self.matricula_1.curso.id)
        self.assertEqual(response.data['periodo'], self.matricula_1.periodo)

    def test_requisicao_put_para_atualizar_matricula(self):
        """
        Verifica se uma requisição PUT para atualizar uma matrícula retorna o status HTTP 200 OK
        e os dados da matrícula atualizada.
        """
        matricula_atualizada = {
            'aluno': self.aluno_1.id,
            'curso': self.curso_1.id,
            'periodo': 'N'
        }
        response = self.client.put(self.detail_url, data=matricula_atualizada)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['periodo'], 'N')

    def test_requisicao_patch_para_atualizar_matricula(self):
        """
        Verifica se uma requisição PATCH para atualizar parcialmente uma matrícula retorna o status HTTP 200 OK
        e os dados da matrícula atualizada.
        """
        matricula_atualizada = {
            'periodo': 'N'
        }
        response = self.client.patch(
            self.detail_url, data=matricula_atualizada)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['periodo'], 'N')

    def test_cache_page_decorator(self):
        """
        Verifica se o decorador cache_page está funcionando, 
        retornando o mesmo resultado da primeira requisição em 60 segundos.
        """
        response_1 = self.client.get(self.list_url)
        self.assertEqual(response_1.status_code, status.HTTP_200_OK)

        matricula_atualizada = {
            'periodo': 'N'
        }
        response_2 = self.client.patch(
            self.detail_url, data=matricula_atualizada)
        self.assertEqual(response_2.status_code, status.HTTP_200_OK)

        response_3 = self.client.get(self.list_url)
        self.assertEqual(response_3.status_code, status.HTTP_200_OK)
        self.assertEqual(response_1.content, response_3.content)
        self.assertNotEqual(response_1.content, response_2.content)
