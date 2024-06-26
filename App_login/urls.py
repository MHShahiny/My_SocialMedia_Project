from django.urls import path
from . import views

# Define the app_name to specify the namespace
app_name = 'App_login'

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.login_page, name='login'),
    path('edit/', views.edit_profile, name='edit'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('user/<str:username>/', views.user, name='user'),
    path('follow/<username>',views.follow,name='follow'),
    path('unfollow/<username>',views.unfollow,name='unfollow'),
    
]
