# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .persona import Persona


class Message(models.Model):
  messageHash = models.TextField(primary_key=True)
  messageType = models.IntegerField()
  messageSig = models.TextField(max_length=2000, blank=True)
  dossierHash = models.TextField()
  bodyHash = models.TextField()
  messagePath = models.TextField(blank=True)
  sender = models.ForeignKey(Persona,
    related_name="outgoing_messages")
  def __str__(self):
    return self.messageHash

class ACLRule(models.Model):
  message = models.ForeignKey(Message, related_name='acl')
  reader = models.ForeignKey(Persona, related_name='incoming_messages')
  key = models.TextField(max_length=2000)
