from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Service, ServiceDescription, Order, Portfolio, Tags
from .serializers import ServiceSerializer, ServiceDescriptionSerializer, OrderSerializer, PortfolioSerializer, \
    TagsSerializer
from django.http import Http404


class ServiceAPIView(APIView):

    def get(self, request, pk=None):
        if pk:
            try:
                service = Service.objects.get(pk=pk)
                serializer = ServiceSerializer(service)
            except Service.DoesNotExist:
                raise Http404
        else:
            services = Service.objects.all()
            serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)


# ServiceDescription View
class ServiceDescriptionAPIView(APIView):

    def get(self, request, pk=None):
        if pk:
            try:
                service_description = ServiceDescription.objects.get(pk=pk)
                serializer = ServiceDescriptionSerializer(service_description)
            except ServiceDescription.DoesNotExist:
                raise Http404
        else:
            service_descriptions = ServiceDescription.objects.all()
            serializer = ServiceDescriptionSerializer(service_descriptions, many=True)
        return Response(serializer.data)


class OrderAPIView(APIView):

    def get(self, request, pk=None):
        if pk:
            try:
                order = Order.objects.get(pk=pk)
                serializer = OrderSerializer(order)
            except Order.DoesNotExist:
                raise Http404
        else:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class TagListAPIView(generics.ListAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


class PortfolioListAPIView(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
