from django.contrib import admin
from .models import Faq_category, Faq, Feedback, WhyUs,Partners, Team,Subscribe, Certificate

# Register your models here.

admin.site.register(Faq_category)
admin.site.register(Faq)
admin.site.register(Feedback)
admin.site.register(WhyUs)
admin.site.register(Partners)
admin.site.register(Team)
admin.site.register(Subscribe)
admin.site.register(Certificate)

