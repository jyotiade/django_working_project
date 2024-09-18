from django.db import models



class AdminModel(models.Model):
    admin_name = models.CharField(max_length=50)
    admin_email = models.EmailField()
    admin_city = models.CharField(max_length=50)
    admin_mobile = models.IntegerField()
    admin_password = models.CharField(max_length=20)


class AdminQuery(models.Model):
    admin_name = models.CharField(max_length=50)
    admin_email = models.EmailField()
    admin_query = models.TextField()