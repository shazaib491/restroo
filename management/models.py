from django.db import models
# python3 manage.py migrate admin <to insialise the table>
# python3 manage.py makemigrations //under suspect
# python3 manage.py makemigrations management < to migrate model into databse>
# python3 manage.py createsupperuser <create db same as phpmyadmin>
# python3 manage.py migrate <to make different changes at a runtime>
class category(models.Model):
    name=models.CharField(max_length=35)
    def __str__(self):
        return self.name

class dish(models.Model):
    cat=models.ForeignKey(category,on_delete=models.CASCADE)
    title=models.CharField(max_length=50,blank=True, null=True)
    price=models.IntegerField(blank=True, null=True)
    mrp=models.IntegerField(blank=True, null=True)
    img=models.ImageField(blank=True, null=True)
    img1=models.ImageField(blank=True, null=True)
    img2=models.ImageField(blank=True, null=True)
    dis=models.TextField(blank=True, null=True)
    avail=models.BooleanField(blank=True, null=True)
    def __str__(self):
        return self.title + '---' + str(self.cat.name)  

class contacts(models.Model):
    name=models.CharField(max_length=50,blank=True, null=True)
    email=models.EmailField(max_length=254,blank=True, null=True)
    subject=models.CharField(max_length=50,blank=True, null=True)
    message=models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name + '---' + str(self.email)
    