""" Project url """
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('Site_app.urls')),

    path('', TemplateView.as_view(
        template_name='Site_app/common/Home.html'),
        name='home'),

    path('about/', TemplateView.as_view(
        template_name='Site_app/common/About.html'),
         name='about'),

    path('users/login/', TemplateView.as_view(
        template_name='registration/login.html'),
         name='login'),
]
