from django.conf.urls import include, url
from django.contrib import admin

from oscar.app import application

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', admin.site.urls),
    
    url(r'', include(application.urls)),
]
