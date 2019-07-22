
from django.utils import timezone
from rest_framework.test import APIClient, APITestCase

from .factories import BookFactory, AuthorFactory


class BooksViewsTest(APITestCase):

    def setUp(self):
        # create 2 books FACTORIES
        b1 = BookFactory.create(
            title='A fairy tale',
            published=timezone.datetime(2018, 7, 8)
        )
        b2 = BookFactory.create(
            title='The Bourne Identity',
            published=timezone.datetime(2011, 3, 1)
        )

    def test_book_api(self):
        response = self.client.get('/books/', format='json')
        self.assertContains(response, 'A fairy tale')
        self.assertContains(response, 'The Bourne Identity')

    def test_book_api_sort_title_ascending(self):
        response = self.client.get('/books/?sort=title&direction=asc', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual([b['title'] for b in response.data],
                         ['A fairy tale', 'The Bourne Identity'])

    def test_book_api_sort_title_descending(self):
        response = self.client.get('/books/?sort=title&direction=desc', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual([b['title'] for b in response.data],
                         ['The Bourne Identity', 'A fairy tale'])

    def test_book_api_sort_date_ascending(self):
        response = self.client.get('/books/?sort=published&direction=asc', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual([b['title'] for b in response.data],
                         ['The Bourne Identity', 'A fairy tale'])

    def test_book_api_sort_date_descending(self):
        response = self.client.get('/books/?sort=published&direction=desc', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual([b['title'] for b in response.data],
                         ['A fairy tale', 'The Bourne Identity'])


class AuthorViewSetTests(APITestCase):

    def setUp(self):
        self.a1 = AuthorFactory()
        self.a2 = AuthorFactory()
        BookFactory(author=self.a1)
        BookFactory(author=self.a1)
        BookFactory(author=self.a1)
        BookFactory(author=self.a2)

    def test_author_api(self):
        response = self.client.get('/authors/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        author1 = response.data[0]
        self.assertEqual(self.a1.name, author1['name'])
        self.assertEqual(self.a1.book_set.count(), len(author1['books']))
        author2 = response.data[1]
        self.assertEqual(self.a2.name, author2['name'])
        self.assertEqual(self.a2.book_set.count(), len(author2['books']))
