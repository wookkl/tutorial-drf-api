from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from users.views import UserList, UserRetrieveView


app_name = "users"

urlpatterns = format_suffix_patterns([
    path(r'', UserList.as_view(), name="user-list"),
    path(r'<int:pk>/', UserRetrieveView.as_view(), name="user-detail"),
])
