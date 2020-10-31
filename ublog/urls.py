from django.contrib import admin
from django.urls import path

from blog.views import IndexView, PostDetailView, NewPostView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index-view'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-view'),
    path('new-post/', NewPostView.as_view(), name='new-post-view'),
]
