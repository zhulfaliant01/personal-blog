from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView

from .models import Post
from .tasks import task_render_markdown


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"
    queryset = Post.objects.all().order_by("-created_at")


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context["post"]

        # Kirim task ke Huey dan ambil hasilnya secara blocking
        result = task_render_markdown(post.is_markdown, post.content)
        rendered_content = result.get(blocking=True)
        context["rendered_content"] = rendered_content
        return context


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "post_form.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        is_markdown = self.request.POST.get("is_markdown") == "on"
        form.instance.author = self.request.user
        form.instance.is_markdown = is_markdown
        return super().form_valid(form)


class PostDeleteDirectView(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect("home")
