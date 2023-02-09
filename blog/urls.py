from . import views
from django.urls import path


urlpatterns = [
    path('reviews/', views.PostList.as_view(), name='reviews')
]
