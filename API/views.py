from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import userData, workSpace, column, card
from .serializers import userDataSerializer, workSpaceSerializer, columnSerializer, cardSerializer, userLogin
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime

# Create your views here.

@api_view(['GET'])
def getUsers(request):
    users = userData.objects.all()
    serializer = userDataSerializer(users, many = True)
    return Response(serializer.data)

# @api_view(['POST'])
# def createUser(request):
#     hash_password = make_password(request.data['password'])
#     request.data['password'] = hash_password
#     serializer = userDataSerializer(data=request.data)
#     if serializer.is_valid():

#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class regiterAPIView(APIView):
    def post(self, request):
        hash_password = make_password(request.data['password'])
        request.data['password'] = hash_password
        serializer = userDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class loginAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = userData.objects.get(email=email)

        if user is None:
            raise AuthenticationFailed('User not found')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        payload = {
            "id": user.id,
            "email": user.email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'message': 'login success',
            'jwt': token
        }
        return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        user = userData.objects.get(id=payload['id']).first()
        serializer = userDataSerializer(user)
        return Response(serializer.data)

class logoutAPIView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response





@api_view(['GET'])
def getWorkspace(request):
    workSpaces = workSpace.objects.all()
    serializer = workSpaceSerializer(workSpaces, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def createWorkspace(request):
    serializer = workSpaceSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getColumns(request):
    columns = column.objects.all()
    serializer = columnSerializer(columns, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def createColumn(request):
    serializer = columnSerializer(data = request.data )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getCards(request):
    cards = card.objects.all()
    serializer = cardSerializer(cards, many = True)
    return Response(serializer.data)


@api_view(['POST'])
def createCard(request):
    serializer = cardSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)



