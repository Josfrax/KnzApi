from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', "is_staff", "is_superuser"]
        #fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True, }, }
