from biblioteca.views import BooksViewSet, UsersViewSet, LoansViewSet
from django.urls import path, include
from rest_framework import routers
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'books', BooksViewSet, basename='books')
router.register(r'users', UsersViewSet, basename='users')
router.register(r'loans', LoansViewSet, basename='loans')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]#