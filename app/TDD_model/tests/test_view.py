from django.test import TestCase, RequestFactory
from django.db.models import QuerySet
from app.TDD_model.models import Animal

class IndexViewTestCase(TestCase):
    def setUp(self):
        request_factory = RequestFactory()
        self.animal = Animal.objects.create(
            name_animal='Leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não',
        )


    def test_index_view_retorna_caracteristicas_do_animal(self):
        '''teste retorna se o index retornar as caracteristicas do animal'''
        response = self.client.get('/',{'buscar':'resultado'})
        caracteristicas_animal_passado = response.context['caracteristicas']
        self.assertIs(type(response.context['caracteristicas']), QuerySet)
        self.assertEqual(caracteristicas_animal_passado[0].name_animal, 'Leão')