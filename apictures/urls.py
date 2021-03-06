from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns=[
    re_path('^$',views.home,name = 'home'),
    re_path('^search/', views.search, name='search'),
    re_path('^image/(?P<image_id>)',views.image,name ='image'),
    re_path('^category/(?P<category_id>)',views.category,name ='category'),
    re_path('^location/(?P<location_id>)',views.location,name ='location'),
    
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)