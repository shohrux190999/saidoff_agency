from rest_framework import serializers
from .models import Faq_category, Faq, Feedback, WhyUs,Partners, Team,Subscribe, Certificate

class Faq_categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq_category
        fields = ('id', 'title')


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ('id', 'questions', 'answers', 'faq_page', 'faq')


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'name', 'comment', 'profession', 'image')


class WhyUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyUs
        fields = ('id', 'title', 'description')


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = ('id', 'image')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'image', 'profession', 'created_at')


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ('id', 'full_name', 'phone_number', 'is_checked', 'created_at')
    

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('id', 'title', 'description', 'image')

