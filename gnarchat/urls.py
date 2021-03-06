from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import website.views

urlpatterns = [
    url(r'^$', website.views.index, name='index'),
    url(r'^post_message$', website.views.post_message),
    url(r'^kill_messages$', website.views.kill_messages),
    url(r'^messages$', website.views.messages),
    path('admin/', admin.site.urls),
]
