from django.contrib import admin
from .models import CharityGuide, CharityImage

@admin.action(description="Mark selected projects as Published")
def mark_as_published(modeladmin, request, queryset):
    queryset.update(is_published=True)

@admin.action(description="Mark selected projects as Unpublished")
def mark_as_unpublished(modeladmin, request, queryset):
    queryset.update(is_published=False)

class CharityImageInline(admin.TabularInline):
    model = CharityImage
    extra = 1  
    readonly_fields = ('uploaded_at',)
    fields = ('image', 'caption', 'uploaded_at')

class CharityGuideAdmin(admin.ModelAdmin):
    # Removed custom form
    list_display = ('myanmar_name','name', 'region', 'is_published', 'created_at')
    list_filter = ('region', 'is_published')
    search_fields = ('myanmar_name','name', 'address', 'notes')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [CharityImageInline]
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

    actions = [
        mark_as_published,
        mark_as_unpublished,
    ]

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

admin.site.register(CharityGuide, CharityGuideAdmin)
