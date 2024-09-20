from django.contrib import admin
from .models import Faq_category, Faq, Feedback, WhyUs,Partners, Team,Subscribe, Certificate
from modeltranslation.admin import TranslationAdmin

# Register your models here.

class Faq_categoryAdmin(TranslationAdmin):
    list_display = ('id', 'title')
admin.site.register(Faq_category,Faq_categoryAdmin)


class FaqAdmin(admin.ModelAdmin):
    list_display = ('id', 'questions', 'faq_page',)
admin.site.register(Faq, FaqAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'comment', 'profession', 'image')
admin.site.register(Feedback, FeedbackAdmin)



class WhyUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
admin.site.register(WhyUs, WhyUsAdmin)


class PartnersAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
admin.site.register(Partners, PartnersAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'profession', 'created_at')
admin.site.register(Team, TeamAdmin)


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number', 'is_checked', 'created_at')
admin.site.register(Subscribe, SubscribeAdmin)


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image')
admin.site.register(Certificate, CertificateAdmin)

