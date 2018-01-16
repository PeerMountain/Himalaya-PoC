# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class SaltedMetaHash(models.Model):
  saltedMetaHash = models.TextField(primary_key=True)

class Container(models.Model):
  containerHash = models.TextField(primary_key=True)
  saltedMetaHashes = models.ManyToManyField(SaltedMetaHash, related_name='containers')
  objectHash = models.TextField(db_index=True)
  containerSig = models.TextField(max_length=2000)
  objectContainerPath = models.TextField()
  createdAt = models.DateTimeField(auto_now_add=True, blank=True)

  def __str__(self):
    return self.containerHash

