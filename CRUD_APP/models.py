from django.db import models

# Create your models here.
class Order(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=50)
    emobile = models.CharField(max_length=12)
    email = models.EmailField()
    eaddress = models.CharField(max_length=200)
    edate = models.DateField()
    