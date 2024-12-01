from .serializers import RegisterSerializers, LoginSerializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response




class RegisrerView(APIView):
     def post(self, request):
        serializer = RegisterSerializers(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = RegisterSerializers(serializer.validated_data['password'])
            user = serializer.save()

            return Response({
                'message': 'User created successfully!',
                'user': user,
            }, status=status.HTTP_201_CREATED)

        else:
            return Response({
                'error_message': 'This email has already exist!',
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            return Response({
                'message': 'User login successfully!',
                'user': user,
            }, status=status.HTTP_200_OK)

        else:
            return Response({
                'error_message': 'Username or password is incorrect!',
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)