from rest_framework import serializers
from chat.models import Message
# from chat.models import Users

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'  

# class ItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = "__all__"