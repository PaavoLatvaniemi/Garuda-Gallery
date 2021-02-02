"""galleria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from UserApp import views as accounts_views
from MainPage import views as MainPage_views

from django.conf.urls import url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', MainPage_views.home, name='home'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='UserApp/login.html'), name='login'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'profile/$', accounts_views.profile, name=('profile')),
    url(r'^group/add/$', accounts_views.AddGroupView.as_view(), name='group_add'),
    url(r'^group/(?P<group_id>[0-9]+)/delete$', accounts_views.group_delete, name='group_delete'),
    url(r'^group/(?P<group_id>[0-9]+)/edit$', accounts_views.GroupEditView.as_view(), name='group_edit'),
    path('upload/', include('upload.urls')),
    path('explorer/', include('explorer.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)