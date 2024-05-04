from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("edit/<int:pk>", views.edit, name="edit"),
    path("detail/<int:pk>", views.detail, name="detail"),
    path("search", views.search, name="search"),
    # path("pets", views.pets, name="pets"),
    path("like", views.like, name="like"),
    path("pet/<int:pk>/comment", views.comment, name="comment"),
    path("organization/<int:pk>", views.pets_by_organization, name="organization"),
    path("favorite", views.favorite, name="favorite"),
    path("my_animals", views.myAnimals, name="my_animals")

]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )