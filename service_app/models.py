from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class ServiceDescription(models.Model):
    service_title = models.ForeignKey(Service, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='service_description')
    description = models.TextField()


class Order(models.Model):
    service_name = models.ForeignKey(Service, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, null=False)
    phone_number = models.CharField(max_length=50, blank=False, null=False)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)




class Portfolio(models.Model):
    service_name = models.ForeignKey(Service, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio')
    url_link = models.URLField(blank=False, null=False)
