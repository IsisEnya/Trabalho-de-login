from rest_framework import viewswts
from contas.models import User
from contas.serializers import UserSerializer

class UserViewSet (viewswts.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 

