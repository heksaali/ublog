from django.contrib import admin
from blog.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    pass

admin.site.register(BlogPost, BlogPostAdmin)