from rest_framework.views import APIView
from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import userData


class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = userData
        fields = ['username', 'password', 'email']

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists")
        return email


    def save(self, request):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        return user

class LoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = userData
        fields = ['username', 'password']

    def validate(self, request):
        username = self.validated_data['username']
        password = self.validated_data['password']
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if not user.check_password(password):
                raise serializers.ValidationError("Password is incorrect")
        else:
            raise serializers.ValidationError("Username is incorrect")
        return user


