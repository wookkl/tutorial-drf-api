from django.urls import path

from users.views import UserList, UserRetrieveView


app_name = "users"

urlpatterns = [
    path(r'', UserList.as_view(), name="user-list"),
    path(r'<int:pk>/', UserRetrieveView.as_view(), name="user-detail"),
]
