from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author


class BookViewSet(ReadOnlyModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        # read query parameters (sort=field, direction=asc|desc)
        direction = self.request.query_params.get('direction', 'asc').lower()
        order_by_name = self.request.query_params.get('sort', '').lower()
        possible_directions = {
            'asc': '',
            'desc': '-'
        }
        if order_by_name:
            order_by_direction = possible_directions.get(direction, 'asc')
            order_by = f"{order_by_direction}{order_by_name}"
            return Book.objects.all().order_by(order_by)
        return Book.objects.all()


class AuthorViewSet(ReadOnlyModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
