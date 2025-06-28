from django.contrib import admin
from .models import FinancialStatement

@admin.action(description="Mark selected statements as published")
def mark_as_published(modeladmin, request, queryset):
    queryset.update(is_published=True)

@admin.action(description="Mark selected statements as not published")
def mark_as_not_published(modeladmin, request, queryset):
    queryset.update(is_published=False)

class FinancialStatementAdmin(admin.ModelAdmin):
    list_display = ('statement_name', 'release_date','is_published','created_at')  
    list_filter = ('release_date',)                        
    search_fields = ('statement_name',)                              
    ordering = ('-release_date',)
    
    actions = [mark_as_published, mark_as_not_published]
        
    def has_module_permission(self, request):
        return request.user.is_staff

    def has_view_permission(self, request, obj=None):
        return request.user.is_staff

    def has_add_permission(self, request):
        return request.user.is_staff  

    def has_change_permission(self, request, obj=None):
        return request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        return request.user.is_staff
    
admin.site.register(FinancialStatement, FinancialStatementAdmin)