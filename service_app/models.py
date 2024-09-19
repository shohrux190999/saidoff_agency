from django.db import models

<<<<<<< HEAD
=======
# Create your models here.
>>>>>>> d20b4f3 (Commit xabari)

class Service(models.Model):
    title = models.CharField(max_length=50)

<<<<<<< HEAD

class ServiceDescription(models.Model):
    service_title = models.ForeignKey(Service, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='service_description')
    description = models.TextField()


class Order(models.Model):
    service_name = models.ForeignKey(Service, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, null=False)
    phone_number = models.CharField(max_length=50, blank=False, null=False)
=======
    def __str__(self):
        return self.title

    
class Order(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    service_name = models.ForeignKey(Service, on_delete=models.CASCADE)
>>>>>>> d20b4f3 (Commit xabari)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)

<<<<<<< HEAD

class Tags(models.Model):
    name = models.CharField(max_length=50)


class Portfolio(models.Model):
    service_name = models.ForeignKey(Service, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio')
    url_link = models.URLField(blank=False, null=False)
    tag = models.ManyToManyField(Tags)
=======
    def __str__(self):
        return self.name


class Service_description(models.Model):
    image = models.ImageField(upload_to = 'media/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    service_typ = models.ForeignKey(Service, on_delete = models.CASCADE)
    def __str__(self):
        return self.title


class Portfolio(models.Model):
    image = models.ImageField(upload_to = 'media/')
    url_link = models.URLField()
    service_name = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.service_name.title
>>>>>>> d20b4f3 (Commit xabari)
