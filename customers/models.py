from django.db import models
from django.contrib.auth.models import User
from management.models import dish


class customers(models.Model):

    c_name = models.CharField(max_length=35, blank=True, null=True)
    c_pay = models.IntegerField(blank=True, null=True)
    c_order = models.TextField(blank=True, null=True)
    c_discount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.c_name + '----' + self.c_pay + '-----'+self.c_order


class add_to_cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    dish = models.ForeignKey(
        dish, on_delete=models.CASCADE, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    confirm = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self):
        return self.user.username


class reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    guests = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length=10)
    email = models.EmailField(blank=True, null=True)
    mob = models.IntegerField(blank=True, null=True)
    confirm = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.name+ str(self.date)+ str(self.time)

class team(models.Model):
    name=models.CharField(blank=True, null=True,max_length=10)
    designation=models.CharField(blank=True, null=True,max_length=10)
    img=models.FileField(blank=True, null=True)
    fb=models.URLField(blank=True, null=True)
    twt=models.URLField(blank=True, null=True)
    insta=models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name + str(self.designation)
    
