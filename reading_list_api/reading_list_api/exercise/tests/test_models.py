
from django.test import TestCase

from ..models import Book, Author, Publisher

class ModelTests(TestCase):

    def test_simple_book(self):
        data = {
            "uid": "eb422d6f-1d2a-4dec-bc97-d0e77e0ed750",
            "cover": "https://lorempixel.com/640/480/?d0e77e0ed750",
            "isbn": "unknown",
            "title": "Un début dans la vie",
            "subtitle": "La Comédie Humaine",
            "author": Author.objects.create(name="Honoré de Balzac"),
            "published": "1844-01-01T00:00:00.000Z"
        }
        book = Book.objects.create(**data)

        self.assertIsNone(book.publisher)
        self.assertIsNone(book.pages)
        self.assertEqual(book.description, "")
        self.assertEqual(book.website, "")

    def test_full_book(self):
        data = {
            "uid": "3ae372e9-b500-4f37-aacf-5569cae3bf77",
            "cover": "https://lorempixel.com/640/480/?5569cae3bf77",
            "isbn": "9781449337711",
            "title": "Designing Evolvable Web APIs with ASP.NET",
            "subtitle": "Harnessing the Power of the Web",
            "author": Author.objects.create(name="Prof. John Doe"),
            "published": "2014-04-07T00:00:00.000Z",
            "publisher": Publisher.objects.create(name="O'Reilly Media"),
            "pages": 538,
            "description": "Design and build Web APIs for a broad range of clients—including browsers and mobile devices—that can adapt to change over time. This practical, hands-on guide takes you through the theory and tools you need to build evolvable HTTP services with Microsoft’s ASP.NET Web API framework. In the process, you’ll learn how design and implement a real-world Web API.",
            "website": "http://chimera.labs.oreilly.com/books/1234000001708/index.html"
        }
        book = Book.objects.create(**data)

        self.assertIsNotNone(book.publisher)
        self.assertEqual(book.pages, 538)
        self.assertEqual(book.description, data['description'])
        self.assertEqual(book.website, data['website'])
