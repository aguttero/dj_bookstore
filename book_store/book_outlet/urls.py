from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("<int:book_db_id>", views.book_detail, name="book_detail_url"),
    path("detail", views.detail)
]
