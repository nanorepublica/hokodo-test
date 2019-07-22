from rest_framework import serializers

from .models import Book, Author, Publisher


class BookSerializer(serializers.ModelSerializer):
    """
    Used to import Books into the database and expose them over the /books endpoint
    """
    author = serializers.CharField(source='author.name')
    publisher = serializers.CharField(source='publisher.name', required=False)
    id = serializers.UUIDField(source='uid')

    class Meta:
        model = Book
        fields = (
            'id',
            'cover',
            'isbn',
            'title',
            'subtitle',
            'author',
            'published',
            'publisher',
            'pages',
            'description',
            'website',
        )

    def create(self, validated_data):
        author_data = validated_data.pop('author', {})
        publisher_data = validated_data.pop('publisher', {})
        author, _ = Author.objects.get_or_create(**author_data)
        validated_data['author'] = author
        if publisher_data:
            publisher, _ = Publisher.objects.get_or_create(**publisher_data)
            validated_data['publisher'] = publisher
        return super().create(validated_data)


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, source='book_set')

    class Meta:
        model = Author
        fields = (
            'name',
            'books'
        )
