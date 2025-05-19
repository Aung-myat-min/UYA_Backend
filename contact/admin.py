from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'ph_number', 'subject', 'created_at', 'is_replied')
    list_filter = ('created_at', 'is_replied')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'ph_number', 'subject', 'message', 'created_at')

    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'ph_number')
        }),
        ('Message Info', {
            'fields': ('subject', 'message', 'created_at', 'is_replied')
        }),
    )

    ordering = ('-created_at',)

    def has_add_permission(self, request):
        return False

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields 
        return self.readonly_fields + ('is_replied',)

admin.site.register(ContactMessage, ContactMessageAdmin)
