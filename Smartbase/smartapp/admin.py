from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'application_id',
        'full_name',
        'email',
        'entrance_exam',
        'score',
        'institution',
        'branch',
        'status',
        'created_at',
    )
    search_fields = ('application_id', 'full_name', 'email')
