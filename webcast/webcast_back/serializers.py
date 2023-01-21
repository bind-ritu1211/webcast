# Third Party Stuff
from django.core.validators import RegexValidator
from rest_framework.serializers import IntegerField, ModelSerializer

# vital stuff
from .models import ConnectMe


class ConnectMeSerializer(ModelSerializer):

    id = IntegerField(required=False)

    def create(self, validated_data):
        return ConnectMe.objects.create(**validated_data)

    class Meta:
        model = ConnectMe
        fields = ['id', 'project_detail', 'email', 'mobile_number']
