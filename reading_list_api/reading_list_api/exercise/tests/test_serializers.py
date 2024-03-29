
from django.test import TestCase

from ..serializers import BookSerializer, AuthorSerializer
from ..models import Book, Author, Publisher

data = {
    "id": "872179f2-4de2-4cde-a259-ee470d83d515",
    "cover": "https://lorempixel.com/640/480/?ee470d83d515",
    "isbn": "9781593275846",
    "title": "Eloquent JavaScript, Second Edition",
    "subtitle": "A Modern Introduction to Programming",
    "author": "Mrs. John Doe",
    "published": "2014-12-14T00:00:00Z",
    "publisher": "No Starch Press",
    "pages": 472,
    "description": "JavaScript lies at the heart of almost every modern web application, from social apps to the newest browser-based games. Though simple for beginners to pick up and play with, JavaScript is a flexible, complex language that you can use to build full-scale applications.",
    "website": "http://eloquentjavascript.net/"
}


class SerializerTests(TestCase):

    def test_book_serializer(self):
        self.assertEqual(Book.objects.count(), 0)
        self.assertEqual(Author.objects.count(), 0)
        self.assertEqual(Publisher.objects.count(), 0)
        serializer = BookSerializer(data=data)
        serializer.is_valid()
        serializer.save()
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Author.objects.count(), 1)
        self.assertEqual(Publisher.objects.count(), 1)

    def test_author_serializer(self):
        serializer = BookSerializer(data=data)
        serializer.is_valid()
        serializer.save()

        author_serializer = AuthorSerializer(instance=Author.objects.first())

        self.assertEqual(author_serializer.data['name'], "Mrs. John Doe")
        self.maxDiff = None
        self.assertEqual(dict(author_serializer.data['books'][0]), data)
