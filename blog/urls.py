
from django.urls import path, include
from . import views

urlpatterns = [
   
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('signup/', views.user_signup, name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="userLogout"),

    path('addBlog/', views.create_post, name = "addBlog"),
    path('editBlog/<int:id>', views.edit_post, name = "editPost"),
    path('delete/<int:id>', views.delete_post, name = "deletePost")
]

