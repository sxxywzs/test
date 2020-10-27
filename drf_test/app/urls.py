from django.urls import path

from app import views

urlpatterns = [
    path('user/',views.user ),
    path('user_view/',views.Users.as_view() ),
    path('user_view/<str:id>/',views.Users.as_view() ),


]
