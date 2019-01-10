from django.contrib import admin

from main.models import Blog


class BlogAdmin(admin.ModelAdmin):

    list_display = ('title', 'date_created', 'last_modified', 'is_draft')


admin.site.register(Blog, BlogAdmin)
