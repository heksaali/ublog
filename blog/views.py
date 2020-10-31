from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import BlogPost
from blog.forms import PostForm

class IndexView(ListView):
    template_name = 'index.html'
    model = BlogPost

class PostDetailView(TemplateView):
    template_name = 'post.html'

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['post'] = get_object_or_404(BlogPost, slug=self.kwargs['slug'])
        return data


class NewPostView(LoginRequiredMixin, FormView):
    template_name = 'new_post.html'
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)