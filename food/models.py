from django.db import models


class FoodInstance(models.Model):
    class Meta:
        permissions = (
            ("can_order", "Can order the drinks"),
            ("can_serve", "Can prepare and serve the drinks"),
        )

class OrderInstance(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    coffee_order = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

class BusinessObject(models.Model):
    business_status = models.CharField(max_length=10)