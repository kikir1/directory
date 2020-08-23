from django.db import models


class Directory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    shortName = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)
    version = models.TextField(unique=True)
    date = models.DateField()

    def __str__(self):
        return self.shortName


class ElementDirectory(models.Model):
    id = models.IntegerField(primary_key=True)
    parentId = models.ForeignKey(Directory, on_delete=models.CASCADE)
    code = models.TextField()
    body = models.TextField()
