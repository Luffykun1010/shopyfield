from django.db import models
from django.contrib.auth.models import User
class Company(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=200) 