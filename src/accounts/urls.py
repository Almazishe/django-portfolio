from django.urls import path


from . import views

urlpatterns = [
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('registration/', views.register, name='registration'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

]