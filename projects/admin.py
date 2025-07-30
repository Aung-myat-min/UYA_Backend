from django.contrib import admin
from .models import Project, ProjectImage


@admin.action(description="Mark selected projects as Published")
def mark_as_published(modeladmin, request, queryset):
    queryset.update(is_published=True)


@admin.action(description="Mark selected projects as Unpublished")
def mark_as_unpublished(modeladmin, request, queryset):
    queryset.update(is_published=False)


@admin.action(description="Mark selected projects as Radio Program")
def mark_as_radio(modeladmin, request, queryset):
    queryset.update(category="Radio Program")


@admin.action(description="Mark selected projects as Monthly Donation")
def mark_as_monthly(modeladmin, request, queryset):
    queryset.update(category="Montly Donation")


@admin.action(description="Mark selected projects as Emergency Response")
def mark_as_emergency(modeladmin, request, queryset):
    queryset.update(category="Emergency Response")

@admin.action(description="Mark selected projects as Kann Lat")
def mark_as_kann(modeladmin, request, queryset):
    queryset.update(category="Kann Lat")
    
@admin.action(description="Mark selected projects as Youth Empowerment")
def mark_as_youth(modeladmin, request, queryset):
    queryset.update(category="Youth Empowerment")

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    readonly_fields = ('uploaded_at',)
    fields = ('image', 'caption', 'uploaded_at')
    show_change_link = False


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'start_date', 'end_date', 'is_published')
    list_filter = ('category', 'is_published', 'start_date')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]
    readonly_fields = ('created_at',)
    ordering = ('-start_date',)

    actions = [
        mark_as_published,
        mark_as_unpublished,
        mark_as_radio,
        mark_as_monthly,
        mark_as_emergency,
        mark_as_kann,
        mark_as_youth
    ]

    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'description', 'category')
        }),
        ('Schedule', {
            'fields': ('start_date', 'end_date')
        }),
        ('Publishing', {
            'fields': ('is_published', 'created_at')
        }),
    )
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

admin.site.register(Project, ProjectAdmin)
