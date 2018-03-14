from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.portfolio_app.urls', namespace='portfolio_app')),
    url(r'^baseball/', include('apps.baseball_app.urls', namespace='baseball_app')),
    url(r'^resQmia/', include('apps.resQmia_app.urls', namespace='resQmia_app')),
]