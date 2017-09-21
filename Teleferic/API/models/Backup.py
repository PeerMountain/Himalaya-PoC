# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Backup(models.Model):
  #Encrypted with key
  description = models.TextField()
  #Encrypted with key
  hash = models.TextField()
  #Passphrased PrivKey
  key = models.TextField()
  sender = models.TextField()

  def __str__(self):
    return self.id.__str__()