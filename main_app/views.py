from django.shortcuts import render
<<<<<<< HEAD
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
=======
from .models import Faq_category, Faq, Feedback, WhyUs,Partners, Team,Subscribe, Certificate
from .serializers import Faq_categorySerializer,FaqSerializer, FeedbackSerializer, WhyUsSerializer, PartnersSerializer, TeamSerializer, SubscribeSerializer, CertificateSerializer
from rest_framework import generics




# Create your views here.

class Faq_categoryList(generics.ListCreateAPIView):
    queryset = Faq_category.objects.all()
    serializer_class = Faq_categorySerializer


class FaqList(generics.ListCreateAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


class FeedbackList(generics.ListCreateAPIView):
>>>>>>> d20b4f3 (Commit xabari)
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


<<<<<<< HEAD

class SubscriberListAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
=======
class WhyUsList(generics.ListCreateAPIView):
    queryset = WhyUs.objects.all()
    serializer_class = WhyUsSerializer


class PartnersList(generics.ListCreateAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer


class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class SubscribeList(generics.ListCreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer


class CertificateList(generics.ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class Faq_categoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faq_category.objects.all()
    serializer_class = Faq_categorySerializer


class FaqDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


class FeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class WhyUsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WhyUs.objects.all()
    serializer_class = WhyUsSerializer


class PartnersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class SubscribeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer


class CertificateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


>>>>>>> d20b4f3 (Commit xabari)
