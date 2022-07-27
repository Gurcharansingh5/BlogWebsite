from django.urls import path,include
from . import views
from . views import *

urlpatterns = [
    path('',views.blogindex,name='blogindex'),
    path('createblog', views.createblog, name='createblog'),
    # path('blogregister',views.blogregister, name='blogregister'),
    # path('bloglogin', views.bloglogin,name='bloglogin'),
    path('editprofile',views.editprofile,name='editprofile'),
    path('bloglogout', views.bloglogout,name='bloglogout'),
    path('blogdelete/<int:id>',views.blogdelete,name='blogdelete'),
    path('readblog/<int:id>',views.readblog,name='readblog'),
    path('blogupdate/<int:id>',views.blogupdate,name='blogupdate'),
    path('blogcomment/<int:id>',views.commentonblog,name = "commentonblog"),
    path('login/',login_page,name='login'),
    path('register/',register_page,name='register'),
    path('token/',token_send,name='token_send'),
    path('success/',success,name='success'),
    path('verify/<auth_token>/',verify,name='verify'),
    path('error/',error_page,name='error'),
]
