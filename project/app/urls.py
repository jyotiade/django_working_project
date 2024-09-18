from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('land/',views.land,name='land'),
    path('register/',views.register,name='register'),
    path("login/",views.login,name='login'),
    # path("query/",views.query,name='query'),
    # path("delete/<int:pk>",views.delete,name='delete'),
    # path("edit/<int:pk>",views.edit,name='edit'),
    # path("update/<int:pk>",views.update,name='update'),
    
]
