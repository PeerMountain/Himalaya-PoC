# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Object(models.Model):
  objectHash = models.TextField(db_index=True)
  message = models.ForeignKey('Message', related_name='_objects')
  createdAt = models.DateTimeField(auto_now_add=True, blank=True)

  def __str__(self):
    return self.objectHash

class SaltedMetaHash(models.Model):
  saltedMetaHash = models.TextField(db_index=True)
  _object = models.ForeignKey(Object, related_name='saltedMetaHashes')
  createdAt = models.DateTimeField(auto_now_add=True, blank=True)

class Container(models.Model):
  containerHash = models.TextField(db_index=True)
  containerSig = models.TextField(max_length=2000)
  objectContainerPath = models.TextField()
  _object = models.ForeignKey(Object, related_name='container')
  createdAt = models.DateTimeField(auto_now_add=True, blank=True)



