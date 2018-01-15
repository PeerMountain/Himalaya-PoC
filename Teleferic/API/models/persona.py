# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Persona(models.Model):
  address= models.TextField(primary_key=True)
  pubkey= models.TextField(unique=True)
  nickname= models.TextField(unique=True)
  createdAt = models.DateTimeField(auto_now_add=True, blank=True)

  def __str__(self):
    return self.address+' ('+self.nickname+')'