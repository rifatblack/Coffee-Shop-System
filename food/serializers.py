from rest_framework import serializers
from .models import OrderInstance

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInstance
        fields = '__all__'