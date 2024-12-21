from django.db import models

# Create your models here.

class Product(models.Model):
    category = models.CharField(max_length=100, null=False, blank= False)
    amount  = models.IntegerField()

    def __str__(self):
        return f"{self.category} - {self.amount}"