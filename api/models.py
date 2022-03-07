from statistics import mode
from time import time
from django.db import models
import datetime



class Note(models.Model):
    id = models.CharField(max_length=128,primary_key=True)
    theBorrower = models.TextField()
    nominal = models.TextField()
    description = models.CharField(max_length=200, blank=True)
    imagePaths = models.ImageField(upload_to='images',default='test.jpg',null=False, blank=False)
    createdTime=  models.DateTimeField(auto_now_add=True)
    editedTime = models.DateTimeField(auto_now=True)
    createdBy = models.TextField()
    lastEditedBy = models.TextField(default='',blank=False, null=False)
    lastSync = models.CharField(max_length=128,blank=True, null=True)
    isDeleted = models.TextField(default='false', null=False, blank=False)
    
    def __str__(self):
        return self.theBorrower[0:50]
    
    class Meta:
        ordering = ['editedTime']