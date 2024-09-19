<<<<<<< HEAD
from packaging.tags import Tag
from rest_framework import serializers
from .models import Service, ServiceDescription, Order, Portfolio, Tags

=======
from rest_framework import serializers
from .models import Service, Order, Service_description, Portfolio
>>>>>>> d20b4f3 (Commit xabari)

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
<<<<<<< HEAD
        fields = '__all__'


class ServiceDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDescription
        fields = '__all__'
=======
        fields = ('id', 'title')
>>>>>>> d20b4f3 (Commit xabari)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
<<<<<<< HEAD
        fields = '__all__'


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'
=======
        fields = ('id', 'name', 'phone_number', 'service_name', 'message', 'created_at', 'is_checked')


class ServiceDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_description
        fields = ('id', 'image', 'title', 'description', 'service_typ')

>>>>>>> d20b4f3 (Commit xabari)


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = ('id', 'image', 'url_link', 'service_name')

>>>>>>> d20b4f3 (Commit xabari)
