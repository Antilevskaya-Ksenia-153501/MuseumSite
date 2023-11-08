from django.db import models
from django.contrib.auth.models import AbstractUser

class Post(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class CustomUser(AbstractUser):
    email = models.EmailField()
    is_customer = models.BooleanField(default = False)
    is_employee = models.BooleanField(default = False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

       
class Customer(CustomUser):

    def __str__(self):
        return self.username
      
      
class Employee(CustomUser):
    date_birth = models.DateField()
    phone_number = models.CharField(max_length=50)
    post = models.OneToOneField(Post, on_delete=models.DO_NOTHING, null=True, default=None)
    image = models.ImageField(upload_to='employee/', null=True, blank=False, default='news/default.png',
                              max_length=100)