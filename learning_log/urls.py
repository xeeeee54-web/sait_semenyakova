
from django.contrib import admin
from django.urls import path
from learning_logs import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("topics/<int:topic_id>/", views.topic, name="topic"),
    path("new_topic/", views.new_topic, name="new_topic"),
]
