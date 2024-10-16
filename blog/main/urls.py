from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include


router = DefaultRouter()
router.register(r"posts", views.PostViewSet, basename="post")


urlpatterns = [
    path("api/", include(router.urls)),
    path("api/users/", views.UserCreate.as_view(), name="user-create"),
]
