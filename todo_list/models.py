from django.db import models

# Create your models here.
class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + '   (' + str(self.completed) + ')'


class Subgroup(models.Model):
    name = models.CharField(max_length=200)
    organisms = models.CharField(max_length=200)

    def __str__(self):
        return self.name
