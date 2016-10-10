from __future__ import unicode_literals

from django.db import models


class Email(models.Model):

    email_id = models.CharField(max_length=128, help_text='Gmail id', unique=True)
    from_address = models.CharField(max_length=128)
    to_address = models.CharField(max_length=128)
    body = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.email_id
