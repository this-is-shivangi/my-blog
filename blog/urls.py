from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list, name='post_list'),

    path('details/',views.post_details, name="post_details"),
    path('login/',views.log, name="login"),
    path('signup/',views.sign, name="signup"),
    path('about/',views.about, name="about"),
    

]