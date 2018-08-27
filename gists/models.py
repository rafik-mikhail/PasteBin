from django.db import models
from pasteBin_project import settings
from django.urls import reverse


class Gists(models.Model):
    sharable = models.BooleanField()
    code = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='gists')
    expiration = models.IntegerField()
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.code[:25]

    def get_absolute_url(self):
        return reverse('gist_detail', args=[str(self.id)])
