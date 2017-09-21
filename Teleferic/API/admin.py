from django.contrib import admin

from .models import Invitation, Registration, Backup

class InvitationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Invitation, InvitationAdmin)

class RegistrationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Registration, RegistrationAdmin)

class BackupAdmin(admin.ModelAdmin):
    pass

admin.site.register(Backup, BackupAdmin)