from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

app_name = 'snippets'

urlpatterns = [
    path(r'', views.snippet_list, name='snippets-list'),
    path(r'<int:pk>/', views.snippet_detail, name='snippets-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
