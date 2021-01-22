from django.urls import path

from snippets import views

app_name = 'snippets'

urlpatterns = [
    path(r'', views.snippet_list, name='snippets-list'),
    path(r'<int:pk>/', views.snippet_detail, name='snippets-detail'),
]
