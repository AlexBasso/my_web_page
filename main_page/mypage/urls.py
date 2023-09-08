from django.contrib import admin
from django.urls import path

from mypage.views import IndexView, CVView, Index2View

app_name = "mypage"

urlpatterns = [
    path("", Index2View.as_view(), name="index2"),
    path("index", IndexView.as_view(), name="index"),
    path("cv", CVView.as_view(), name="cv"),
    path("cv2", CVView.as_view(), name="cv2"),
]