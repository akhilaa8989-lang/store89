from django.db import models

# Create your models here.
class CustomerModel(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    phone=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    password=models.CharField(max_length=8)
    confrim_password=models.CharField(max_length=8)

    def __str__(self):
        return self.name

class productsModoel(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    product_img = models.ImageField(upload_to='products/',null=True,blank=True)

    def __str__(self):
        return self.product_name