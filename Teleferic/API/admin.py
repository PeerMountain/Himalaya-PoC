# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from API.models import *

class PersonaAdmin(admin.ModelAdmin):
    pass
    
class MessageAdmin(admin.ModelAdmin):
    pass

class ACLAdmin(admin.ModelAdmin):
    pass

admin.site.register(Persona, PersonaAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(ACLRule, ACLAdmin)