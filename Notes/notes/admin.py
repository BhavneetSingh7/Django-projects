from django.contrib import admin
from .models import Note, ApiToken

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ('user','title','created_at')

class ApiTokenAdmin(admin.ModelAdmin):
    list_display = ('user','key','og_key','created_at')

admin.site.register(Note,NoteAdmin)
admin.site.register(ApiToken,ApiTokenAdmin)