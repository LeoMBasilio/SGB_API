from .models import Books, Users, Loans
from rest_framework import serializers
from .validators import validate_cpf, validate_email, validate_phone, validate_name

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

    def validate(self, data):
        if not validate_name(data['author']):
            raise serializers.ValidationError('Author name must contain only letters')
        return data

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

    def validate(self, data):
        if not validate_name(data['name']):
            raise serializers.ValidationError('Name must contain only letters')
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError('Invalid CPF')
        if not validate_email(data['email']):
            raise serializers.ValidationError('Invalid email')
        if not validate_phone(data['phone']):
            raise serializers.ValidationError('Invalid phone number')
        return data
    
class LoansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loans
        fields = '__all__'