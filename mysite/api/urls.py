from django.urls import path
from . import views

urlpatterns = [
    path('blogpost/', views.BlogPostListCreate.as_view(), name='blogpost'),
    path('blogpost/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name='blogpost-retrieve-update-destroy'),
]