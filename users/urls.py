from django.urls import path
from .views import signup, login, logout

urlpatterns = [
    path("signup/", view=signup, name="signup"),
    path("login/", view=login, name="login"),
    path("logout/", view=logout, name="logout"),
]
