from .models import User
from rest_framework import viewsets, response, status
from .serializers import UserSerializer 


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request,):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        print('***************')
        print(request.data)
        print('***************')
        user.set_senha(serializer.validated_data.get('senha'))
        user.save()
        headers = self.get_success_headers(serializer.data)

        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
