from django.db import models
from django.urls import reverse


class Message(models.Model):
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("api_messages:message_detail", args=[self.pk])
