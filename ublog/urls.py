from django.contrib import admin
from django.urls import path

from blog.views import IndexView, PostDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-view')
]
