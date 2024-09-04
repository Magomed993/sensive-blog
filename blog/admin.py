from webbrowser import register

from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ['post', 'author']
    list_display = ('text', 'published_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ['author', 'likes', 'author']
    list_display = ['title', 'published_at']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']

# admin.site.register(Post, PostAdmin)
# admin.site.register(Tag, TagAdmin)
# admin.site.register(Comment, CommentAdmin)
