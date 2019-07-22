import logging
from rest_framework.exceptions import ValidationError

from config import celery_app

from .client import book_client
from .models import Book
from .serializers import BookSerializer


@celery_app.task(name='ingest-books-to-db')
def ingest_books_to_db():
    """
    Use a celery task to import books to the database in the background
    """
    data = book_client.get()
    # Start of dealing with not reimporting existing Books. Serializers would need updating as well
    # existing = Book.objects.filter(uid__in=[b['id'] for b in data['books']])
    # serializer = BookSerializer(instance=existing, data=data['books'], many=True)
    serializer = BookSerializer(data=data['books'], many=True)
    try:
        serializer.is_valid(raise_exception=True)
    except ValidationError as exc:
        logging.error('Import Validation Failed: %s', exc)
        return
    serializer.save()
