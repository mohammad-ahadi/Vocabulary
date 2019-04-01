from django.db import models


class Word(models.Model):
    english = models.CharField(max_length=255)
    persian = models.CharField(max_length=255)
    definition = models.TextField(default='')
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.english
