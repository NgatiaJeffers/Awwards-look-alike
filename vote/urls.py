from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name = "projects"),
    path("project/post/", views.post, name = "post"),
    path("user/profile/", views.profile, name = 'profile'),
    path("project/<int:id>/", views.project_detail, name = "details"),
    path("search/projects/results/", views.search, name = "search"),
    path("logout/", views.logout, name = "logout"),
]