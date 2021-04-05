from rest_framework_mongoengine import serializers
from TASBackend.models import Member

class MemberSerializer (serializers.DocumentSerializer):
    class Meta:
        model = Member 
        fields = '__all__'