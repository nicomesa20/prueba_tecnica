from django.shortcuts import render
from datetime import datetime
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from ..serializers.user import UserSerializer
from cerberus import Validator
from django.db.models import Q


# Create your views here.

class UserAPI(APIView):

    def post(self, request):

        def to_date(date): return datetime.strptime(date, '%Y-%m-%d')
        validator = Validator({
            'email': {'required': True, 'type': 'string'},
            'first_name': {'required': True, 'type': 'string'},
            'last_name': {'required': True, 'type': 'string'},
            'birth_date': {'required': True, 'type': 'date', 'coerce': to_date},
            'password': {'required': True, 'type': 'string'},            
        })
        if not validator.validate(request.data):
            return Response({
                'code': 'Cuerpo de la peticion invalida',
                'data': validator.errors
            }, status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data=request.data)
        

        if not serializer.is_valid():
            return Response({
                'code': 'Cuerpo de la peticion invalida',
                'data': serializer.errors
            }, status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(
            Q(email=request.data['email'])
        ).first()

        if user:
            return Response({
                'code': 'Este usuario ya esta registrado',
            }, status.HTTP_409_CONFLICT)

        user = serializer.create(validated_data=request.data)

        return Response(status.HTTP_201_CREATED)
        

