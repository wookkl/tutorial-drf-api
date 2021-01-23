from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from core.views import api_root

urlpatterns = format_suffix_patterns([
    path('', api_root)
])
