from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

app_name = 'snippets'

urlpatterns = format_suffix_patterns([
    path(r'', views.SnippetList.as_view(), name='snippet-list'),
    path(r'<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path(r'<int:pk>/highlight/', views.SnippetHighlight.as_view(),
         name='snippet-highlight'),
])
