from django.db import models


# Create your models here.
class OrganizationDetails(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, default='')
    description = models.TextField()
    longitude = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    google_maps_url = models.CharField(max_length=100)
    conductor = models.CharField(max_length=100, default='')
    assigned_to = models.CharField(max_length=100, default='')
    rank = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'OrganizationDetails'
