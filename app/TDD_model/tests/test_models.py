from django.test import TestCase, RequestFactory
from app.TDD_model.models import Animal


class AnimalModelTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            name_animal='Leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não',
        )

    def test_animal_cadastrado_com_caracteristicas(self):
        '''teste que verifica se o animal esta cadastrado com suas caracteristicas'''
        self.assertEqual(self.animal.name_animal, 'Leão')