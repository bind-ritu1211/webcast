# Third Party Stuff
from rest_framework import status, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# vital Stuff
from . import models, serializers


@permission_classes((AllowAny, ))
class ConnectMeViewSet(viewsets.ModelViewSet):
    queryset = models.ConnectMe.objects.all()
    serializer_class = serializers.ConnectMeSerializer
    http_method_names = ['post']

    @action(detail=False, methods=['POST'])
    def mail(self, request):
        serializer = self.get_serializer(data=request.data['message'])
        if serializer.is_valid():
          models.ConnectMe.objects.create(**serializer.validated_data)
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
