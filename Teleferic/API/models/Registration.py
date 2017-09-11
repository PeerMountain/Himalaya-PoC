# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .Invitation import Invitation

class Registration(models.Model):
  invitation = models.ForeignKey(Invitation)
  pubkey = models.TextField()
  address = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return self.invitation.sender + ' -> ' + self.address