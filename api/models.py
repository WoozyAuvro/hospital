from django.db import models

class esp(models.Model):
    data = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Data: {self.data}, Created: {self.created}"

class espTemp(models.Model):
    temp = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Data: {self.data}, Created: {self.created}"