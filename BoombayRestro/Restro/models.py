from django.db import models

# Create your models here.
class category(models.Model):
    title = models.CharField(max_length=200)

class menuItem(models.Model):
    title = models.CharField(max_length=255,db_index=True)
    price = models.DecimalField(decimal_places=2,max_digits=6)
    featured = models.BooleanField(default=True)
    category = models.ForeignKey(category,on_delete=models.PROTECT)

