from django.db import models

# Create your models here.

class user_tbl(models.Model) :
    user_id     = models.CharField(primary_key=True, max_length=50)
    user_pwd    = models.CharField( max_length=50)
    user_name   = models.CharField(max_length=50)
