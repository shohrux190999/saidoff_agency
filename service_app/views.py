from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Service, ServiceDescription, Order, Portfolio
from .serializers import ServiceSerializer, ServiceDescriptionSerializer, OrderSerializer, PortfolioSerializer
from django.http import Http404


# Service View
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

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            service = Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            raise Http404
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            service = Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            raise Http404
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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

    def post(self, request):
        serializer = ServiceDescriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            service_description = ServiceDescription.objects.get(pk=pk)
        except ServiceDescription.DoesNotExist:
            raise Http404
        serializer = ServiceDescriptionSerializer(service_description, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            service_description = ServiceDescription.objects.get(pk=pk)
        except ServiceDescription.DoesNotExist:
            raise Http404
        serializer = ServiceDescriptionSerializer(service_description, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            service_description = ServiceDescription.objects.get(pk=pk)
        except ServiceDescription.DoesNotExist:
            raise Http404
        service_description.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Order View
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

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Portfolio View
class PortfolioAPIView(APIView):

    def get(self, request, pk=None):
        if pk:
            try:
                portfolio = Portfolio.objects.get(pk=pk)
                serializer = PortfolioSerializer(portfolio)
            except Portfolio.DoesNotExist:
                raise Http404
        else:
            portfolios = Portfolio.objects.all()
            serializer = PortfolioSerializer(portfolios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PortfolioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            portfolio = Portfolio.objects.get(pk=pk)
        except Portfolio.DoesNotExist:
            raise Http404
        serializer = PortfolioSerializer(portfolio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            portfolio = Portfolio.objects.get(pk=pk)
        except Portfolio.DoesNotExist:
            raise Http404
        serializer = PortfolioSerializer(portfolio, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            portfolio = Portfolio.objects.get(pk=pk)
        except Portfolio.DoesNotExist:
            raise Http404
        portfolio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
