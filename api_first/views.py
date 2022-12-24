from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import UserRegisterSerializer
from .aitu import vse



class HandleToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        if not created:
            token.delete()
            token = Token.objects.create(user=user)
        return Response({'token': token.key})

@api_view(['POST'])
@permission_classes((AllowAny,))
def register(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.create_user(serializer.validated_data['username'],None,serializer.validated_data['password'])
        Token.objects.get_or_create(user=user)
        return Response(status=201)
    else:
        return Response(serializer.errors)


@api_view(['POST'])
@permission_classes((AllowAny,))
def overall_score(request):
    return Response(vse(request.data['address']))
