from contas.models import User
from rest_framework import  serializers 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','nome','cep','email')

