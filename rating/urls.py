from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('rate-img/', rate_img, name="rate")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)