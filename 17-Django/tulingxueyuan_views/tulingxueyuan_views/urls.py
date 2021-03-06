"""tulingxueyuan_views URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from teacher_app import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('teacher/', views.teacher),
    path('v2_exp/', views.v2_exception),

    path('v10_1/', views.v10_1),
    path('v10_2/', views.v10_2),
    path('v11/', views.v11, name='v11'),

    path('v8/', views.v8_get),

    path('v9_get/', views.v9_get),
    path('v9_post/', views.v9_post),

    path('render_test/', views.render_test),
    path('render2_test/', views.render2_test),
    path('render3_test/', views.render3_test),

    path('render1_to_test/', views.render4_test),

    path('get404/', views.get404),
]
