# -*- coding: utf-8 -*-
from django.db import models

class Base(models.Model):
    timestamp_create = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True

class User(Base):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
class Trade(Base):
    type = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    symbol = models.CharField(max_length=255)
    shares = models.IntegerField(blank=False)
    price = models.DecimalField(max_digits=2, decimal_places=1)


    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.symbol


