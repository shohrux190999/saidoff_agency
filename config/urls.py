"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main_app.views import (
    WhyusListAPIView, WhyusDestroyAPIView,
    PartnersListAPIView, PartnersDestroyAPIView,
    TeamsRetrieveUpdateDestroyAPIView,
    CertificatesListCreateAPIView, CertificatesDestroyAPIView,
    FAQCategoryListCreateAPIView, FAQCategoryRetrieveUpdateDestroyAPIView,
    FAQRetrieveUpdateDestroyAPIView,
    FeedbackListAPIView, FeedbackDestroyAPIView,
    SubscriberRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # WhyUs
    path('whyus/', WhyusListAPIView.as_view(), name='whyus-list'),
    path('whyus/<int:pk>/delete/', WhyusDestroyAPIView.as_view(), name='whyus-delete'),

    # Partners
    path('partners/', PartnersListAPIView.as_view(), name='partners-list'),
    path('partners/<int:pk>/delete/', PartnersDestroyAPIView.as_view(), name='partners-delete'),

    # Teams
    path('teams/<int:pk>/', TeamsRetrieveUpdateDestroyAPIView.as_view(), name='teams-detail'),

    # Certificates
    path('certificates/', CertificatesListCreateAPIView.as_view(), name='certificates-list-create'),
    path('certificates/<int:pk>/delete/', CertificatesDestroyAPIView.as_view(), name='certificates-delete'),

    # FAQ Category
    path('faq-categories/', FAQCategoryListCreateAPIView.as_view(), name='faqcategory-list-create'),
    path('faq-categories/<int:pk>/', FAQCategoryRetrieveUpdateDestroyAPIView.as_view(), name='faqcategory-detail'),

    # FAQ
    path('faqs/<int:pk>/', FAQRetrieveUpdateDestroyAPIView.as_view(), name='faq-detail'),

    # Feedback
    path('feedback/', FeedbackListAPIView.as_view(), name='feedback-list'),
    path('feedback/<int:pk>/delete/', FeedbackDestroyAPIView.as_view(), name='feedback-delete'),

    # Subscriber
    path('subscribers/<int:pk>/', SubscriberRetrieveUpdateDestroyAPIView.as_view(), name='subscriber-detail'),
]
