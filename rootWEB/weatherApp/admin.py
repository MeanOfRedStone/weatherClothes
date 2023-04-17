from django.contrib import admin
from .models import *

# Photo 클래스를 inline으로 나타낸다.

# Register your models here.

admin.site.register(user_tbl)
admin.site.register(CLOTHES_INFO)

