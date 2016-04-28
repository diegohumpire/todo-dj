from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    state = models.BooleanField()
    publish_date = models.DateTimeField(auto_now_add=True, editable=False)
    user = models.ForeignKey(User, related_name='tasks')

    class Meta:
        ordering = ('publish_date',)

    def __unicode__(self):
        return unicode(self.title)

class UserExtend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_fb_id = models.CharField(max_length=250)