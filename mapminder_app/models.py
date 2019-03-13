from django.db import models


class Chart(models.Model):
    name = models.CharField(max_length=50)
    longname = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    shortname = models.CharField(max_length=200)
    filename = models.FileField(upload_to='charts/')

    def __str__(self):
        return self.shortname

