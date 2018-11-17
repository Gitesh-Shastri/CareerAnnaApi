from django.db import models

# Create your models here.
class ca_category(models.Model):

    CATEGORY_NAME = models.CharField(max_length=250) 	
    ACTIVE_STATUS = models.CharField(max_length=10)	
    PRIORITY_STATUS = models.IntegerField()	
    CREATED_DATE = models.DateTimeField()	
    cimage = models.CharField(max_length=1000)

    def __str__(self):
        return self.CATEGORY_NAME


