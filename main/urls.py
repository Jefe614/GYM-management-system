from django.urls import path
from .import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('pricing/', views.pricing, name='pricing'),
    path('contacts/', views.contacts, name='contacts'),
    path('user_account/', views.user_account, name='user_account'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('settings/', views.settings, name='settings'),
    path('logout/', LogoutView.as_view(), name='logout'),
]