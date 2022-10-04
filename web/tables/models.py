from django.db import models

class LootfarmModel(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    have = models.IntegerField()
    max = models.IntegerField()

class TradeggModel(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    have = models.IntegerField()
    max = models.IntegerField()

