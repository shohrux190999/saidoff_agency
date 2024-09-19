from django.db import models


<<<<<<< HEAD
class WhyUs(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()



class Partners(models.Model):
    image = models.ImageField(upload_to='partners', null=False, blank=False)


class Teams(models.Model):
    name = models.CharField(max_length=50, null=False)
    profession = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='teams')


class Subscriber(models.Model):
    full_name = models.CharField(max_length=50, null=False)
    phone_number = models.CharField(max_length=20, null=False)
    is_checked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)



class Certificates(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to='certificates', null=False, blank=False)

class Feedback(models.Model):
    comment = models.TextField()
    name = models.CharField(max_length=50, null=False)
    profession = models.CharField(max_length=50)
    image = models.ImageField(upload_to='feedback')
    created_at = models.DateTimeField(auto_now_add=True)


class FAQ_Category(models.Model):
    title = models.CharField(max_length=50, null=False)



class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    faq_category = models.ForeignKey(FAQ_Category, on_delete=models.CASCADE)
=======
# Create your models here.

class Faq_category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Faq(models.Model):
    questions = models.TextField()
    answers = models.TextField()
    faq_page = models.CharField(max_length=50)
    faq = models.ForeignKey(Faq_category, on_delete = models.CASCADE)

    def __str__(self):
        return self.questions

class Feedback(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField()
    profession = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name

class WhyUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Partners(models.Model):
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.image

class Team(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/')
    profession = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name

class Subscribe(models.Model):
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    is_checked = models.BooleanField(default=False)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.full_name

class Certificate(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title






>>>>>>> d20b4f3 (Commit xabari)

