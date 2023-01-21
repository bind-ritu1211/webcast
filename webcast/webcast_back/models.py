from django.db import models
from django.contrib.postgres.fields import CIEmailField
from django.utils.translation import gettext_lazy as _


# Create your models here.



class ConnectMe(models.Model):
    project_detail = models.CharField(max_length=30)
    email = CIEmailField(_("email address"))
    mobile_number = models.IntegerField(max_length=12)


    def __str__(self):
        return str(self.project_detail) 
