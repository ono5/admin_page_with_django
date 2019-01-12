from django.contrib import admin
from django.db.models import Count
from django.utils import timezone

from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportModelAdmin
from leaflet.admin import LeafletGeoAdmin
from rangefilter.filter import DateTimeRangeFilter

from main.models import Blog, Comment, Category, Place
from main.resources import CommentResource


# class CommentInline(admin.TabularInline):
class CommentInline(admin.StackedInline):

    model = Comment
    fields = ('text', 'is_active')
    # Attach add another comment
    extra = 1
    classes = ('collapse', ) # turn on or off comment


class BlogAdmin(SummernoteModelAdmin):

    list_display = ('title',
                    'date_created',
                    'last_modified',
                    'is_draft',
                    'days_since_creation',
                    'no_of_comments',)
    list_filter = (
        'is_draft',
        ('date_created', DateTimeRangeFilter),
    )
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
            'fields': ('is_draft', 'categories'),
            'description': 'Opstions to configure blog creation',
            'classes': ('collapse', ), # turn on or off advance option
        })
    )

    summernote_fields = ('body',)
    inlines = (CommentInline, )
    filter_horizontal = ('categories', )

    def get_actions(self, request):
        actions = super().get_actions(request)
        try:
            del actions['delete_selected']
        except KeyError:
            pass
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        """Override queryset"""
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(comments_count=Count('comments'))
        return queryset

    def no_of_comments(self, blog):
        """Inform comment number"""
        return blog.comments_count
    no_of_comments.admin_order_field = 'comments_count'

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


# class CommentAdmin(admin.ModelAdmin):
class CommentAdmin(ImportExportModelAdmin):

    list_display = ('blog', 'text', 'date_created', 'is_active')
    # You can edit item without into fix page
    list_editable = ('text', 'is_active', )
    list_per_page = 20
    # list_filter = ('blog', ) # default filter
    list_filter = (
        ('blog', RelatedDropdownFilter),
    )
    resource_class = CommentResource
    list_select_related = ('blog', )
    raw_id_fields = ('blog', )

# Register setting content
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
admin.site.register(Place, LeafletGeoAdmin)

