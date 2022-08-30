from django.test import TestCase
from aluraflix.models import Programa

class ProgramaModelCase(TestCase):
    def setUp(self):
        self.programa = Programa(
            titulo = 'Procurando ninguém',
            data_lancamento = '2003-05-04'
        )
        
    def teste_verifica_atributos_do_programa(self):
        """Teste que verifica os atributos de um programa com valores default"""
        self.assertEqual(self.programa.titulo, 'Procurando ninguém')
        self.assertEqual(self.programa.tipo, 'F')
        self.assertEqual(self.programa.data_lancamento, '2003-05-04')
        self.assertEqual(self.programa.likes, 0)
        self.assertEqual(self.programa.dislikes, 0)