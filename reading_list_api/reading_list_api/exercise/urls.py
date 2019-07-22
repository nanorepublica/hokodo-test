from rest_framework import routers
from .views import BookViewSet, AuthorViewSet

app_name = "exercise"
router = routers.SimpleRouter()

router.register(r'books', BookViewSet, basename='book')
router.register(r'authors', AuthorViewSet, basename='author')

urlpatterns = router.urls
