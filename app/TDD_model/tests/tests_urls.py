from django.test import TestCase, LiveServerTestCase, RequestFactory
from django.urls import reverse
import time
from app.TDD_model.views import *
from selenium import webdriver
from selenium.webdriver.common.by import By

class AnimaisURLSTestCase(LiveServerTestCase):
    def setUp(self):
        self.factory = RequestFactory()


    def test_rota_url_utiliza_view_index(self):
        '''teste unitário para urls index'''
        request = self.factory.get('/')
        with self.assertTemplateUsed('TDD_model/pages/index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)