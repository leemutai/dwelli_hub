from django.urls import path

from . import views

urlpatterns = [
    path('user', views.user, name="user"),
    path('users', views.all_users, name="all"),
    path('search', views.search_user, name="search"),
    path('user/<int:user_id>', views.user_details, name="details"),
    path('user/delete/<int:user_id>', views.user_delete, name="delete"),
    path('user/update/<int:user_id>', views.user_update, name="update"),

    path('realtor', views.realtor, name="realtor"),
    path('realtors', views.all_realtors, name="all"),
    path('search', views.search_realtor, name="search"),
    path('realtor/<int:realtor_id>', views.realtor_details, name="details"),
    path('realtor/delete/<int:realtor_id>', views.realtor_delete, name="delete"),
    path('realtor/update/<int:realtor_id>', views.realtor_update, name="update"),



]