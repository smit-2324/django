from django.db import models

#DataFlair Models
class student(models.Model):
    enroll = models.CharField(max_length = 20)
    name = models.CharField(max_length = 10)
    email = models.EmailField(blank = True)
    cont  = models.CharField(max_length=14)
    address = models.TextField()
    picture = models.ImageField()
   
def __str__(self):
        return self.name