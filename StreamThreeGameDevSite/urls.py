"""StreamThreeGameDevSite URL Configuration

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
from django.views.static import serve
from .settings import MEDIA_ROOT
from GameDev import views
from paypal.standard.ipn import urls as donation_urls
from donations import views as donation_views
from products import views as product_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.get_index, name='index.html'),
    url(r'', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'', include('accounts.urls')),

    # payment urls
    url(r'^hardtoguessurl/', include(donation_urls)),
    url(r'^paypal-return', donation_views.paypal_return),
    url(r'^paypal-cancel', donation_views.paypal_cancel),
    url(r'^products/$', product_views.all_products),
]
