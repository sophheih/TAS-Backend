from rest_framework_mongoengine import serializers
from TASBackend.models import dailyMenu
from TASBackend.models import dish
class MenuSerializer (serializers.DocumentSerializer):
    class Meta:
        model = dailyMenu
        fields = '__all__'

class DishSerializer (serializers.DocumentSerializer):
    class Meta:
        model = dish
        fields = '__all__'