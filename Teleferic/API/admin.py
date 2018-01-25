# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from API.models import *

class PersonaAdmin(admin.ModelAdmin):
    pass
    
class ACLInline(admin.TabularInline):
    model = ACLRule
    extra = 0

class ContainerInline(admin.StackedInline):
    model = Container
    extra = 0

class MessageAdmin(admin.ModelAdmin):
    inlines = [ACLInline]

class ContainerAdmin(admin.ModelAdmin):
    pass

class ACLAdmin(admin.ModelAdmin):
    pass

admin.site.register(Persona, PersonaAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Container, ContainerAdmin)