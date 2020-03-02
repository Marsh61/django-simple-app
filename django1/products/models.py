from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(decimal_places=2,max_digits=10000)
    summary = models.TextField(default="hello") #blake means required
    featured = models.BooleanField(default=False) #null =True, default=True, or use makemigrations then set a defualt value

    def get_absolute_url(self):
        return reverse("products:product-view",kwargs={"id":self.id})
