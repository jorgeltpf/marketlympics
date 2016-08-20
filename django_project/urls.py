
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from mark_lympics.forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('mark_lympics.urls')),
    url(r'^login/$', views.login, {'template_name': 'login.html'},
        name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),
]
