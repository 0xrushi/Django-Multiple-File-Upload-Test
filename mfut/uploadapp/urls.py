from django.conf.urls import url

from uploadapp.views import BlogView

urlpatterns = [
    url(r'^$', BlogView.as_view(), name='blog')
]