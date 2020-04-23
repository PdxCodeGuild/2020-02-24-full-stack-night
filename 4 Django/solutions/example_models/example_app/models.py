from django.db import models

class User(models.Model):
  first_name = models.CharField(blank = False, default = 'first', max_length=100)
  last_name = models.CharField(blank = False, default = 'last', max_length=100)
  age = models.IntegerField(blank = False, default = 0)
  favorite_pet = models.CharField(null = True, blank = True, max_length=100)
