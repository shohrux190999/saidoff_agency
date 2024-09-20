
from modeltranslation.translator import register, TranslationOptions
from .models import Faq_category, Faq, Feedback, WhyUs, Team,Subscribe, Certificate

@register(Faq_category)
class Faq_categoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = ('questions', 'answers',)


@register(Feedback)
class FeedbackTranslationOptions(TranslationOptions):
    fields = ('name', 'comment',)


@register(WhyUs)
class WhyUsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

@register(Team)
class TeamTranslationOptions(TranslationOptions):
    fields = ('name', 'profession',)


@register(Subscribe)
class SubscribeTranslationOptions(TranslationOptions):
    fields = ('full_name',)


@register(Certificate)
class CertificateTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)




