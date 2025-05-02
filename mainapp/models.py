from django.db import models


class Product(models.Model):

 name = models.CharField(max_length = 255) 
 price = models.FloatField()
 desc = models.TextField(max_length =500)
 img = models.ImageField(upload_to = 'products/' )
 stock = models.PositiveBigIntegerField()
