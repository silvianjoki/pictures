from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns=[
    re_path('^$',views.home,name = 'home'),
    # re_path(r'^search/', views.search_results, name='search_results'),
    # re_path(r'^image/(?P<image_id>\d+)',views.image,name ='image'),
    # re_path(r'^category/(?P<category_id>\d+)',views.category,name ='category'),
    # re_path(r'^location/(?P<location_id>\d+)',views.location,name ='location'),
    
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)