from django.db import models

# Create your models here.
class chapter_name(models.Model):

    CATEGORY_ID = models.CharField(max_length=10000)	
    SUB_CATEGORY_ID = models.CharField(max_length=100) 	
    EXAM_ID = models.CharField(max_length=100)	
    CHAPTER_NAME = models.CharField(max_length=100)	
    ACTIVE_STATUS = models.CharField(max_length=40)	
    CREATED_DATE = models.DateTimeField()

    def __str__(self):
        return self.CHAPTER_NAME