from rest_framework import status, viewsets, permissions
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from api.usecase.login.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class LoginViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    @action(methods=['POST'], detail=False, url_path='login', url_name='login')
    def login(self, request):
        # user = self.get_object()
        user = get_object_or_404(User, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)

        token, _ = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user, many=False)
        return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            user.set_password(serializer.data['password'])
            user.save()

            token = Token.objects.create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.username = request.data['username']
        user.email = request.data['email']
        user.set_password(request.data['password'])
        user.save()
        new_serializer = UserSerializer(user, many=False)
        return Response(new_serializer.data, status=status.HTTP_200_OK)