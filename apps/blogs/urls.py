from django.urls import path

from .views import CreatePostView, PostDeleteDirectView, PostDetailView, PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("post/<str:pk>", PostDetailView.as_view(), name="post_detail"),
    path("create", CreatePostView.as_view(), name="create_post"),
    path("post/<str:pk>/delete/", PostDeleteDirectView.as_view(), name="post_delete"),
]
