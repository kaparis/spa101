from django.db import models

# Create your models here.

# class Songs(models.Model):
#     # song title
#     title = models.CharField(max_length=255, null=False)
#     # name of artist or group/band
#     artist = models.CharField(max_length=255, null=False)

#     def __str__(self):
#         return "{} - {}".format(self.title, self.artist)

# Car Make Class
class Make (models.Model):
    name = models.CharField(max_length=255, null=False)
    Description = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.name, self.Description)
    
    def __repr__(self):
        return "{} - {}".format(self.name, self.Description)

# Car Model Class
class Model (models.Model):
    name = models.CharField(max_length=255, null=False)
    year = models.DateField()
    make = models.ForeignKey(Make, on_delete = models.CASCADE, default=None)

    def __str__(self):
        return "I am a Model Class"

    def __repr__(self):
        return "REPR"