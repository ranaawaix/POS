from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user_accounts.models import User
from user_accounts.api.serializers import CreateUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class CreateUserAPIView(APIView):
    @swagger_auto_schema(request_body=CreateUserSerializer)
    def post(self, request, format=None):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'msg': 'Registration Successful', 'token': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
