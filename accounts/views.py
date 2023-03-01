from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class UsersView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
    
    def get(self, request):
        """
        show non-staff users.
        """
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class UserView(APIView):
    def get(self, request, pk):
        """
        show details of non-staff user.
        """
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=HTTP_200_OK)
        except:
            return Response(serializer.errors, status=HTTP_404_NOT_FOUND)
        
    def put(self, request, pk):
        user = User.objects.get(id=pk)
        user_serialized = UserSerializer(user, data=request.data, partial=True)
        if user_serialized.is_valid():
            user_serialized.save()   
            return Response(user_serialized.data, status=HTTP_200_OK)
        return Response(user_serialized.errors, status=HTTP_400_BAD_REQUEST)
    
    