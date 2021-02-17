from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from django.urls import reverse, resolve
from .forms import UserC


from .models import Book, Review
from .views import sign

class Userclass(TestCase):
    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self) -> None:
        self.book=Book.objects.create(title='Django',author='Shaxzod',price=123)
        self.user=get_user_model().objects.create(
            username='Shaxa',
            email='reviewuser@email.com',
            password='testpass123'

        )
        self.review=Review.objects.create(
            book=self.book,
            author=self.user,
            review='Groosha'
        )

    def test_review(self):
        self.assertEqual(self.book.title,'Django')
        self.assertEqual(self.book.author,'Shaxzod')
        self.assertEqual(self.book.price,123)

    def test_book(self):
        response=self.client.get(self.book.get_absolute_url())
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'books/book_detail.html')
        self.assertNotContains(response,'Ali')

