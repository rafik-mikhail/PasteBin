from django.urls import path
from . import views


urlpatterns = [
    path('', views.gist_list_view, name='gist_list'),
    path('<int:pk>/edit/', views.GistUpdateView.as_view(), name='gist_edit'),
    path('<int:pk>/', views.gist_detail_view, name='gist_detail'),
    path('<int:pk>/delete/', views.GistDeleteView.as_view(), name='gist_delete'),
    path('new/', views.gist_create_view, name='gist_new'),
]
