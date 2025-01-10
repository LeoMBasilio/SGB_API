from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Users(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Loans(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    loan_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    returned = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.name} - {self.book.title}'