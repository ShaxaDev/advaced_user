from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from django.urls import reverse, resolve

from userPRO.views import home


class Userclass(TestCase):

    def setUp(self) -> None:
        url=reverse('home')
        self.response=self.client.get(url)

    def test_create_user(self):
        User=get_user_model()
        user=User.objects.create(
            username='Shaxzod',
            email='will@email.com',
            password='testpass123',
            is_superuser=True
        )

        self.assertTrue(user.is_superuser)

    def test_get(self):
        self.assertEquals(self.response.status_code,200)
        self.assertTemplateUsed(self.response,'home.html')

    def test_home_page(self):
        self.assertEquals(self.response.status_code,200)

    def test_home_get(self):
        self.assertContains(self.response,'Hello')

    def test_resolve_home_page(self):
        view=resolve('/')
        self.assertEquals(view.func,home)