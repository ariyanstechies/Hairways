from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import index
from home.salons import salon_details, SalonCreateView
from home.accounts import UserSignUpView


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, index)

    def test_create_salon_url_resolves(self):
        url = reverse('new_salon')
        self.assertEqual(resolve(url).func.view_class, SalonCreateView)

    def test_salon_details_url_resolves(self):
        url = reverse('show_salon', args=['sample-salon-slug'])
        self.assertEqual(resolve(url).func, salon_details)

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class, UserSignUpView)
