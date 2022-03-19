from pyexpat import model
from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.serializers import ModelSerializer
from .models import MobileUser, DataSupir, Note

class UserSerializer(ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username',]
            )
        ]

class MobileUserSerializer(ModelSerializer):
    class Meta:
        model = MobileUser
        fields = '__all__'

class DataSupirSerializer(ModelSerializer):
    class Meta:
        model = DataSupir
        fields = ['idSup','namaSupir','passSupir','jenis','noPol']
class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'