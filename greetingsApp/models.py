from django.db import models


class Greetings(models.Model):
    name = models.CharField(max_length=60, null=False)
    number_greetings = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.name
