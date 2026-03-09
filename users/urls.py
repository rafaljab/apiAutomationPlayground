from django.urls import path
from .views import UserDeleteView

urlpatterns = [
    path("delete/", UserDeleteView.as_view(), name="user-delete"),
]
