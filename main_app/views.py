from django.shortcuts import render
from main_app.models import WhyUs, Partners, Teams, Certificates, FAQ, Feedback, FAQ_Category, Subscriber
from main_app.serializer import (
    WhyusSerializer, PartnersSerializer, TeamsSerializer, CertificatesSerializer,
    FAQSerializer, FeedbackSerializer, FAQCategorySerializer, SubscriberSerializer
)
from rest_framework import generics, status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
# WhyUs Views
class WhyusListAPIView(generics.ListAPIView):
    queryset = WhyUs.objects.all()
    serializer_class = WhyusSerializer

class WhyusDestroyAPIView(generics.DestroyAPIView):
    queryset = WhyUs.objects.all()
    serializer_class = WhyusSerializer

# Partners Views
class PartnersListAPIView(generics.ListAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer

class PartnersDestroyAPIView(generics.DestroyAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer

# Teams Views
class TeamsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer

# Certificates Views
class CertificatesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Certificates.objects.all()
    serializer_class = CertificatesSerializer

class CertificatesDestroyAPIView(generics.DestroyAPIView):
    queryset = Certificates.objects.all()
    serializer_class = CertificatesSerializer

# FAQ Category Views
class FAQCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = FAQ_Category.objects.all()
    serializer_class = FAQCategorySerializer

class FAQCategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ_Category.objects.all()
    serializer_class = FAQCategorySerializer

# FAQ Views
class FAQRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

# Feedback Views
class FeedbackListAPIView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class FeedbackDestroyAPIView(generics.DestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

# Subscriber Views
class SubscriberRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
