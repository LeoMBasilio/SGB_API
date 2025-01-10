from .models import Books, Users, Loans
from django.contrib import admin

class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pages', 'genre', 'language', 'publication_date', 'isbn')
    list_display_links = ('title', 'author')
    list_per_page = 10
    search_fields = ('title', 'author', 'genre', 'language', 'isbn')

admin.site.register(Books, BooksAdmin)

class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'email', 'phone', 'address')
    list_display_links = ('name', 'cpf')
    list_per_page = 10
    search_fields = ('name', 'cpf', 'email', 'phone', 'address')

admin.site.register(Users, UsersAdmin)

class LoansAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'loan_date', 'return_date', 'returned')
    list_display_links = ('user', 'book')
    list_per_page = 10
    search_fields = ('user__name', 'book__title')

admin.site.register(Loans, LoansAdmin)
#