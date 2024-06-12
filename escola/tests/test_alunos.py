from rest_framework.test import APITestCase
from django.urls import reverse
from django.conf import settings
from rest_framework import status
from escola.models import Aluno
import os


class AlunoTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Alunos-list')
        self.detail_url = reverse('Alunos-detail', args=[1])
        self.aluno_1 = Aluno.objects.create(
            nome='João da Silva',
            rg='123456789',
            cpf='12345678901',
            data_nascimento='2000-01-01',
            celular='11999999999'
        )
        self.aluno_2 = Aluno.objects.create(
            nome='Maria da Costa',
            rg='987654321',
            cpf='98765432101',
            data_nascimento='1995-05-15',
            celular='21988888888'
        )

    def test_requisicao_get_para_listar_alunos(self):
        """
        Verifica se uma requisição GET para a URL de alunos retorna o status HTTP 200 OK,
        indicando que a lista de alunos foi obtida com sucesso.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_aluno(self):
        """
        Verifica se uma requisição POST para a criação de um novo aluno retorna HTTP 201
        CREATED, indicando que o aluno foi criado.
        """
        novo_aluno = {
            'nome': 'José Santos',
            'rg': '456789123',
            'cpf': '45678912301',
            'data_nascimento': '1998-10-20',
            'celular': '12977777777'
        }
        response = self.client.post(self.list_url, data=novo_aluno)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_get_para_detalhar_aluno(self):
        """
        Verifica se uma requisição GET para detalhar um aluno retorna o status HTTP 200 OK
        e os dados do aluno correto.
        """
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], self.aluno_1.nome)

    def test_requisicao_put_para_atualizar_aluno(self):
        """
        Verifica se uma requisição PUT para atualizar um aluno retorna o status HTTP 200 OK
        e os dados do aluno atualizado.
        """
        aluno_atualizado = {
            'nome': 'João da Silva (Atualizado)',
            'rg': '123456789',
            'cpf': '12345678901',
            'data_nascimento': '2000-01-01',
            'celular': '11999999999'
        }
        response = self.client.put(self.detail_url, data=aluno_atualizado)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'João da Silva (Atualizado)')

    def test_requisicao_delete_para_deletar_aluno(self):
        """
        Verifica se uma requisição DELETE para deletar um aluno retorna o status HTTP 204 NO CONTENT
        indicando que o aluno foi deletado com sucesso.
        """
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_post_para_criar_aluno_com_foto(self):
        """
        Verifica se uma requisição POST para a criação de um novo aluno com uma foto retorna HTTP 201
        CREATED, indicando que o aluno foi criado.
        """
        novo_aluno = {
            'nome': 'José Santos',
            'rg': '456789123',
            'cpf': '45678912301',
            'data_nascimento': '1998-10-20',
            'celular': '12977777777',
            'foto': open(os.path.join(settings.BASE_DIR, 'images_test/image01.jpg'), 'rb')
        }
        response = self.client.post(
            self.list_url, data=novo_aluno, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_put_para_atualizar_aluno_com_foto(self):
        """
        Verifica se uma requisição PUT para atualizar um aluno com uma nova foto retorna o status HTTP 200 OK
        e os dados do aluno atualizado com a nova foto.
        """
        aluno_atualizado = {
            'nome': 'João da Silva (Atualizado)',
            'rg': '123456789',
            'cpf': '12345678901',
            'data_nascimento': '2000-01-01',
            'celular': '11999999999',
            'foto': open(os.path.join(settings.BASE_DIR, 'images_test/image01.jpg'), 'rb')
        }
        response = self.client.put(
            self.detail_url, data=aluno_atualizado, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'João da Silva (Atualizado)')
