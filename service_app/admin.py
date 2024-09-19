from django.contrib import admin
<<<<<<< HEAD
from service_app.models import Order, Portfolio, ServiceDescription, Service, Tags
from main_app.models import *

# Register your models here.

admin.site.register(Order)
admin.site.register(Portfolio)
admin.site.register(ServiceDescription)
admin.site.register(Service)
admin.site.register(FAQ)
admin.site.register(FAQ_Category)
admin.site.register(WhyUs)
admin.site.register(Partners)
admin.site.register(Teams)
admin.site.register(Subscriber)
admin.site.register(Certificates)
admin.site.register(Feedback)
admin.site.register(Tags)
=======
from .models import Service, Order, Service_description, Portfolio

# Register your models here.


admin.site.register(Service)
admin.site.register(Order)
admin.site.register(Service_description)
admin.site.register(Portfolio)
>>>>>>> d20b4f3 (Commit xabari)
