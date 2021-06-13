from rest_framework_mongoengine import serializers
from TASBackend.models import constantMenu

class constMenuSerializer (serializers.DocumentSerializer):
    class Meta:
        model = constantMenu
        fields = '__all__'