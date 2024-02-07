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
    path('trainer_create/', views.trainer_create, name='trainer_form'),
    path('trainer_list/',views.trainer_list, name='trainer_list'),
    path('trainer/<int:pk>/',views.trainer_detail, name='trainer_detail'),
    path('trainer/<int:pk>/update/',views.trainer_update, name='trainer_update'),
    path('trainer/<int:pk>/delete/',views.trainer_delete, name='trainer_delete'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('get_started_basic/', views.basic_plan_page, name='basic_plan_page'),
    path('get_started_pro/', views.get_started_pro, name='get_started_pro'),
    path('get_started_premium/', views.get_started_premium, name='get_started_premium'),
    path('basic_plan/', views.basic_plan, name='basic_plan'),
    path('contact/', views.contact_form_submission, name='contact_form_submission'),

]