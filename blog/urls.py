from . import views
from django.urls import path


urlpatterns = [
    path('reviews/', views.PostList.as_view(), name='reviews'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
