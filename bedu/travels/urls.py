from django.contrib.auth import views as auth_views
from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.index, name = "index"),
    path('login/',auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page="/login/"),name = "logout"),
    path('tour/eliminar/<int:idTour>/', views.eliminar_tour, name="eliminar_tour"),
]
