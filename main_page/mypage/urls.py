from django.contrib import admin
from django.urls import path

from mypage.views import IndexView


app_name = "mypage"

urlpatterns = [
    path("", IndexView.as_view(), name="index")
]