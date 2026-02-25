from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    # path('login/', views.user_login),
    path('profile/', views.profile),
    path('logout/', views.user_logout),
    path('search-trains/', views.search_trains),
    path('jwt-login/', views.jwt_login),
    path('jwt-profile/', views.jwt_profile),




]
