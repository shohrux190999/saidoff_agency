from django.contrib import admin
from service_app.models import Order, Portfolio, ServiceDescription, Service
# Register your models here.

admin.site.register(Order)
admin.site.register(Portfolio)
admin.site.register(ServiceDescription)
admin.site.register(Service)
