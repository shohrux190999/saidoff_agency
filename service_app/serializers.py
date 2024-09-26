from rest_framework import serializers
from .models import Service, ServiceDescription, Order, Portfolio


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDescription
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'
