from django.urls import path
from .views import create_posts_and_comments, like_unlike_post, PostDeleteView, PostUpdateView

app_name = 'posts'

urlpatterns = [
    path('', create_posts_and_comments, name='main-post-view'),
    path('liked/', like_unlike_post, name='like-post-view'),
    path('<pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('<pk>/update/', PostUpdateView.as_view(), name='post-update'),
]