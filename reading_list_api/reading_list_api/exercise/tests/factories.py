import uuid
import factory
import factory.fuzzy
from django.utils import timezone

from ..models import Book, Author


class AuthorFactory(factory.DjangoModelFactory):
    name = factory.Faker("name")

    class Meta:
        model = Author


class BookFactory(factory.DjangoModelFactory):
    author = factory.SubFactory(AuthorFactory)
    uid = factory.LazyFunction(uuid.uuid4)
    published = factory.fuzzy.FuzzyDateTime(timezone.datetime(2000, 1, 1, tzinfo=timezone.utc))

    class Meta:
        model = Book
