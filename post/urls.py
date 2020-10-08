from django.conf.urls import url
from . import views

# add url to the post app
urlpatterns = [
    url(r'^$', views.index, name='index')
]
