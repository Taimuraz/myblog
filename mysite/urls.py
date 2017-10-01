from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)), # url connects url and view function
    url(r'', include('blog.urls')),
]
