from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^proj_1/', include('proj_1.urls')),
    url(r'^proj_2/', include('proj_2.urls')),
    url(r'^admin/', admin.site.urls),
]
