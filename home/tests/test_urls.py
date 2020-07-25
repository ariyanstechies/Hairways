from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import index, salon_details
from home.clients import ClientSignUpView
from home.owners import SalonCreateView, OwnerSignUpView


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, index)

    def test_create_salon_url_resolves(self):
        url = reverse('new_salon')
        self.assertEqual(resolve(url).func.view_class, SalonCreateView)

    def test_salon_details_url_resolves(self):
        url = reverse('salon_details', args=['sample-salon-slug'])
        self.assertEqual(resolve(url).func, salon_details)

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class, ClientSignUpView)

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class, OwnerSignUpView)
