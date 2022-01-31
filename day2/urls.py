
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from new.views import*
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup,name="signup"),
    path('',nav,name="nav"),
    path('login/',login,name="login"),
    path('delete/',delete,name="delete"),
    path('insertstudent/',insertstudent,name="insertstudent"),
    path('selectall/',selectall,name="selectall"),
    path('selectbyname/',selectbyname,name="selectbyname"),
    path('update/',update,name="update"),
    path('homenav/',homenav,name="homenav"),

]
