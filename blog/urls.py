from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home_page'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path(
        'delete/<int:pk>',
        views.delete_comment,
        name="delete_comment",
        ),
    path(
        'edit/<int:pk>',
        views.edit_comment,
        name="edit_comment",
    ),
    path('post_detail/edit_post/<int:pk>/', views.edit_post, name='edit_post'),

]
