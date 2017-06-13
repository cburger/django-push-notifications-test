from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework import status, permissions, serializers
from rest_framework.response import Response


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    key = serializers.ReadOnlyField()

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if user:
            if not user.is_active:
                raise serializers.ValidationError('This account has been disabled')
        else:
            raise serializers.ValidationError('The email address or password you have entered is incorrect.')
        attrs['user'] = user
        return attrs


class LoginView(GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            token, created = Token.objects.get_or_create(user=serializer.validated_data['user'])
            return Response(self.get_serializer({'key': token.key}).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
