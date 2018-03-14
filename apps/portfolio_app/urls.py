from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='portfolio_app_index'),
]