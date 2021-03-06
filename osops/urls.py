"""osops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from app.userprofile import views as user_views

from app.assets import urls as host_urls
# from app.assets.rest import urls as rest_urls
from app.index import urls as index_urls
from app.layout import urls as layout_urls
from app.userprofile import urls as user_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^accounts/login/', user_views.LoginHandler, name='login'),
    url(r'^accounts/logout/', user_views.LogoutHandler, name='logout'),

    url(r'', include(layout_urls)),
    url(r'^index/', include(index_urls)),
    url(r'^assets/', include(host_urls)),
    url(r'^user/', include(user_urls)),
    # url(r'^api/', include(rest_urls)),
]
