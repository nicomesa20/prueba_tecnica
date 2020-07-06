from rest_framework import serializers
from ...models.user import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password
import copy


class UserSerializer(serializers.ModelSerializer):
    ''' Creates an user'''

    email = serializers.EmailField(
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        data = copy.deepcopy(validated_data) 
        
        data['email'] = data['email'].lower()
        data['password'] = make_password(validated_data['password'])

        user = User.objects.create(**data)
        user.save()

        return user





    