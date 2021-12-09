
from django.contrib import admin
from django.urls import path

from facebook.views import play1
from facebook.views import play2
from facebook.views import my_profile
from facebook.views import fail, help, warn
from facebook.views import newsfeed
from facebook.views import detail_feed
from facebook.views import pages
from facebook.views import new_feed
from facebook.views import edit_feed, remove_feed
from facebook.views import new_page
#from facebook.views import detail_page
#from facebook.views import edit_page, remove_page

urlpatterns = [
    path('admin/', admin.site.urls),

    path('play1/', play1),
    path('play2/', play2),
    path('dogeunchoi/profile/', my_profile),
    path('fail/', fail),
    path('help/', help),
    path('warn/', warn),

    path('', newsfeed),
    path('new/', new_feed),
    path('feed/<pk>/', detail_feed),
    path('feed/<pk>/remove/', remove_feed),
    path('feed/<pk>/edit/', edit_feed),

    path('pages/', pages),
    path('pages/new/', new_page),
]
