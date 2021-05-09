from rest_framework_mongoengine import serializers
from TASBackend.models import dish

class DishSerializer (serializers.DocumentSerializer):
    class Meta:
        model = dish
        fields = '__all__'