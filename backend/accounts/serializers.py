from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import *
User = get_user_model()
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class AuthorSerializer(serializers.ModelSerializer):
    
    user = UserRegisterSerializer()
    class Meta:
        model = Author
        fields = ('resume','education','biography','phone','user') 

    # def create(self, validated_data):
    #     user_data = validated_data.pop('user')
    #     author = Author.objects.create(**validated_data)
    #     User.objects.create(**user_data)
    #     author.save()
    #     return author

    def create(self, validated_data):
        # Extract the user data and create the User instance first
        user_data = validated_data.pop('user')
        user = UserRegisterSerializer().create(validated_data=user_data)

        # Create the Author instance and link it to the created User instance
        author = Author.objects.create(user=user, **validated_data)
        
        return author

    