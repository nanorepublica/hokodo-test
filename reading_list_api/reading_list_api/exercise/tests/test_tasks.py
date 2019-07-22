import requests_mock
import pytest
from django.test import TestCase, override_settings

from ..models import Book, Author, Publisher
from ..tasks import ingest_books_to_db

JSON_DATA = {
    "books": [
        {
            "id": "872179f2-4de2-4cde-a259-ee470d83d515",
            "cover": "https://lorempixel.com/640/480/?ee470d83d515",
            "isbn": "9781593275846",
            "title": "Eloquent JavaScript, Second Edition",
            "subtitle": "A Modern Introduction to Programming",
            "author": "Mrs. John Doe",
            "published": "2014-12-14T00:00:00.000Z",
            "publisher": "No Starch Press",
            "pages": 472,
            "description": "JavaScript lies at the heart of almost every modern web application, from social apps to the newest browser-based games. Though simple for beginners to pick up and play with, JavaScript is a flexible, complex language that you can use to build full-scale applications.",
            "website": "http://eloquentjavascript.net/"
        },
        {
            "id": "89cae71c-fbe5-445c-8299-6de7a88ea5ab",
            "cover": "https://lorempixel.com/640/480/?6de7a88ea5ab",
            "isbn": "9781449331818",
            "title": "Learning JavaScript Design Patterns",
            "subtitle": "A JavaScript and jQuery Developer's Guide",
            "author": "Prof. John Doe",
            "published": "2012-07-01T00:00:00.000Z",
            "publisher": "O'Reilly Media",
            "pages": 254,
            "description": "With Learning JavaScript Design Patterns, you'll learn how to write beautiful, structured, and maintainable JavaScript by applying classical and modern design patterns to the language. If you want to keep your code efficient, more manageable, and up-to-date with the latest best practices, this book is for you.",
            "website": "http://www.addyosmani.com/resources/essentialjsdesignpatterns/book/"
        }
    ]
}


class TaskTests(TestCase):

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    def test_simple_task_run(self):
        with requests_mock.Mocker() as m:
            m.register_uri('GET', 'https://hokodo-frontend-interview.netlify.com/data.json', json=JSON_DATA)
            ingest_books_to_db.delay()
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Author.objects.count(), 2)
        self.assertEqual(Publisher.objects.count(), 2)

    @pytest.mark.skip(reason="Functionality not yet implemented")
    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    def test_double_task_run(self):
        with requests_mock.Mocker() as m:
            m.register_uri('GET', 'https://hokodo-frontend-interview.netlify.com/data.json', json=JSON_DATA)
            ingest_books_to_db.delay()
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Author.objects.count(), 2)
        self.assertEqual(Publisher.objects.count(), 2)

        # when run again, we would expect nothing to change
        with requests_mock.Mocker() as m:
            m.register_uri('GET', 'https://hokodo-frontend-interview.netlify.com/data.json', json=JSON_DATA)
            ingest_books_to_db.delay()
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Author.objects.count(), 2)
        self.assertEqual(Publisher.objects.count(), 2)
