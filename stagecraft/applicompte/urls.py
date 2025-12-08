from django.urls import path
from django.contrib.auth import views as auth_views
from applicompte import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='applicompte/login.html'), name='login'),
    path('logout/', views.deconnexion, name="logout"),
    path('connexion/', views.connexion),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='applicompte/password_reset.html', 
        email_template_name='applicompte/password_reset_email.html'), name='password_reset'),
    path('rest/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='applicompte/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(
        template_name='applicompte/password_reset_done.html'), name='password_reset_done'),
    path('reset_done', auth_views.PasswordResetCompleteView.as_view(
        template_name='applicompte/password_reset_complete.html'), name='password_reset_complete'),

]