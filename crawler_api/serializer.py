from rest_framework_mongoengine import serializers
from TASBackend.models import dailyMenu

class MenuSerializer (serializers.DocumentSerializer):
    class Meta:
        model = dailyMenu
        fields = '__all__'