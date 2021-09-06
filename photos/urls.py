from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/all', views.all_categories_gallery, name="all_categories_gallery"),
    path('location/all', views.all_locations_gallery, name="all_locations_gallery"),
    re_path(r'^category/(\d+)$', views.gallery_by_category, name ="gallery_by_category"),
    re_path(r'^location/(\d+)$', views.gallery_by_location, name ="gallery_by_location"),
    path('search/', views.search_category, name='search_category'),
    re_path(r'^ajax/photo-detail/(\d+)$', views.photo_detail, name="photo_detail"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)