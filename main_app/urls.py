from django.urls import path
from main_app.views import *
urlpatterns = [
    path('logout/',logou,name='logout'),
    path('logout1/',logou2,name='logou2'),
    path('see_commety/',commety,name='commety'),
    path('create_user/',create,name='create_user'),
    path('login/',log1,name='log1'),
    path('log2/',log2,name='log2'),
    path('',admin_user_login,name='admin_user_login')
]