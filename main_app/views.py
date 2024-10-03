from django.shortcuts import render
from main_app.models import WhyUs, Partners, Teams, Certificates, FAQ, Feedback, FAQ_Category, Subscriber
from main_app.serializer import (
    WhyusSerializer, PartnersSerializer, TeamsSerializer, CertificatesSerializer,
    FAQSerializer, FeedbackSerializer, FAQCategorySerializer, SubscriberSerializer
)
from rest_framework import generics


class WhyusListAPIView(generics.ListAPIView):
    queryset = WhyUs.objects.all()
    serializer_class = WhyusSerializer


class PartnersListAPIView(generics.ListAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer



class TeamsListAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer


# Certificates Views
class CertificatesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Certificates.objects.all()
    serializer_class = CertificatesSerializer


class FAQCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = FAQ_Category.objects.all()
    serializer_class = FAQCategorySerializer


class FAQListAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer



class FeedbackListAPIView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer



class SubscriberListAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
