from django.db import models

# Create your models here.
class stock(models.Model):
    news= models.CharField(max_length=1000,default='SOME STRING')
    def __str__(self):
        return self.news


#username : admin
#pass: hesham123