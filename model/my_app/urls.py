from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('login/',views.login),
    path('logout/',views.logout),
    path('page/',views.page),
    path('post/',views.post),
    path('song/',views.song),
    path('show_user_data/',views.show_user_data),
    path('show_page_data/',views.show_page_data),
    path('show_post_data/',views.show_post_data),
    path('show_song_data/',views.show_song_data),
]