from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('profile/',views.profile, name='profile'),
    path('profile/ass_class',views.ass_class, name='ass_class'),
    path('profile/ass-class-google',views.ass_class_g, name='ass_class_g'),
    path('google-class/',views.profile_g, name='profile_g'),
    # path('google-class/<gk>/',views.google_posts, name='google_posts'),
    path('piazza/',views.profile_p, name='profile_p'),
    path('piazza/<pk>/',views.piazza_posts, name='piazza_posts'),
    path('logout/',views.user_logout,name='logout')
    ]
