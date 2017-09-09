# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Invitation(models.Model):
  content = models.TextField()
  key = models.TextField()
  used = models.BooleanField(default=False)
  sender = models.TextField()

  def __str__(self):
    return self.id.__str__()