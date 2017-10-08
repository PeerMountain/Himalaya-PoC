# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .persona import Persona


class Message(models.Model):
  messageHash = models.TextField(primary_key=True)
  messageType = models.IntegerField()
  dossierHash = models.TextField()
  bodyHash = models.TextField()
  sender = models.ForeignKey(Persona,
    related_name="outgoing_messages")
  acl = models.ManyToManyField(Persona, 
    through='ACLRule', 
    through_fields=('message','reader'),
    related_name="incoming_messages")

  def __str__(self):
    return self.messageHash

class ACLRule(models.Model):
  message = models.ForeignKey(Message)
  reader = models.ForeignKey(Persona)
  key = models.TextField()
