from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    description= models.CharField(max_length=500)

    def __str__(self):
        return self.name + ' ' + self.description