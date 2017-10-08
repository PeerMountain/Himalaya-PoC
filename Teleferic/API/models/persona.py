# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Persona(models.Model):
  address = models.TextField(primary_key=True)
  pubkey = models.TextField()

  def __str__(self):
    return self.address