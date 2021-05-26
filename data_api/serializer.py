from rest_framework_mongoengine import serializers
from TASBackend.models import data

class DataSerializer (serializers.DocumentSerializer):
    class Meta:
        model = data
        fields = '__all__'