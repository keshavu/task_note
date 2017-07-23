# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Note(models.Model):
    """
    Create Notes for task
    """
    title = models.CharField(max_length=200)
    additional_text = models.TextField()
    published_date = models.DateTimeField(
            auto_now_add=True)

    def __str__(self):
        return self.title