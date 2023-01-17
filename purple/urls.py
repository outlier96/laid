from django.urls import path
from . import views
app_name="purple"

urlpatterns = [ 
    path('login_user',views.login_user,name="login"),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    path('dashboard', views.dashboard, name='dashboard'),
] 