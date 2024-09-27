from django.db import models

class item(models.Model):
    name=models.CharField(max_length=200)
    create=models.DateTimeField(auto_now_add=True)