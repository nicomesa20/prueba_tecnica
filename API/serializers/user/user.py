from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

USER = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        validators = [UniqueValidator(queryset=USER.objects.all())]
    )
    username = serializers.CharField(
        validators = [UniqueValidator(queryset=USER.objects.all())]
    )
    
    class Meta:

        model = USER
        fields = '__all__'

    def create(self, data):
        user = USER.objects.create(data)
        user.save()





    