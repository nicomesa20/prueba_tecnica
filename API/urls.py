from django.urls import path
from .views.user import UserAPI

urlpatterns = [
    path('user/', UserAPI.as_view())
]
