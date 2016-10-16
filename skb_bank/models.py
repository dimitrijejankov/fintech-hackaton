from django.db import models


class Clients(models.Model):
    age = models.IntegerField()
    bank = models.IntegerField()
    buy_insurance = models.IntegerField()
    citizenship = models.IntegerField()
    income = models.IntegerField()
    insurance = models.IntegerField()
    intention = models.IntegerField()
    interest = models.IntegerField()
    type = models.IntegerField()
    urgency = models.IntegerField()
