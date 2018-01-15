# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .message import Message


class Container(models.Model):
  message = models.ForeignKey(Message, related_name='containers')
  containerHash = models.TextField(db_index=True)
  objectHash = models.TextField(db_index=True)
  containerSig = models.TextField(max_length=2000)
  objectContainerPath = models.TextField()
  retainUntil = models.TextField(max_length=2000)
  validUntil = models.TextField(max_length=2000)

  def __str__(self):
    return self.containerHash

class SaltedMetaHash(models.Model):
  container = models.ForeignKey(Container, related_name='saltedMetaHashes')
  saltedMetaHash = models.TextField(db_index=True)
