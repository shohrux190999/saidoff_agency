from django.urls import path
from main_app.views import (
    WhyusListAPIView,
    PartnersListAPIView,
    TeamsListAPIView,
    CertificatesListCreateAPIView,
    FAQCategoryListCreateAPIView,
    FAQListAPIView,
    FeedbackListAPIView,
    SubscriberListAPIView
)

urlpatterns = [
    path('whyus/', WhyusListAPIView.as_view(), name='whyus-list'),
    path('partners/', PartnersListAPIView.as_view(), name='partners-list'),

    path('teams/<int:pk>/', TeamsListAPIView.as_view(), name='teams-detail'),

    path('certificates/', CertificatesListCreateAPIView.as_view(), name='certificates-list'),

    path('faq-categories/', FAQCategoryListCreateAPIView.as_view(), name='faqcategory-list-create'),

    path('faqs/<int:pk>/', FAQListAPIView.as_view(), name='faq-detail'),

    path('feedback/', FeedbackListAPIView.as_view(), name='feedback-list'),

    path('subscribers/<int:pk>/', SubscriberListAPIView.as_view(), name='subscriber-detail'),
]
