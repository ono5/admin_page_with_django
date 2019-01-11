from django.contrib import admin
from django.utils import timezone

from django_summernote.admin import SummernoteModelAdmin

from main.models import Blog


class BlogAdmin(SummernoteModelAdmin):

    list_display = ('title', 'date_created', 'last_modified', 'is_draft', 'days_since_creation')
    list_filter = ('is_draft', 'date_created')
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title', )}
    list_per_page = 50
    actions = ('set_blogs_to_published', )
    date_hierarchy = 'date_created'
    fieldsets = (
        (None, {
            'fields': (('title', 'slug'), 'body'),
        }),
        ('Advanced options', {
            'fields': ('is_draft', ),
            'description': 'Opstions to configure blog creation',
        })
    )

    summernote_fields = ('body',)

    def days_since_creation(self, blog):
        """diff date to show on the list"""
        diff = timezone.now() - blog.date_created
        return diff.days
    days_since_creation.short_description = 'DAY ACTIVE'

    def get_ordering(self, request):
        if request.user.is_superuser:
            return ('title', '-date_created')
        return ('title',)

    def set_blogs_to_published(self, request, queryset):
        """Set Action behave"""
        count = queryset.update(is_draft=False)
        self.message_user(request, '{} blogs have been published successfully.'.format(count))
    set_blogs_to_published.short_description = 'Mark selected blog as published'


admin.site.register(Blog, BlogAdmin)
