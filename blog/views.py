from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from blog.models import BlogPost

class IndexView(ListView):
    template_name = 'index.html'
    model = BlogPost

class PostDetailView(TemplateView):
    template_name = 'post.html'

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['post'] = get_object_or_404(BlogPost, slug=self.kwargs['slug'])
        return data
