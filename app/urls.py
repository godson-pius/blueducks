from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('booking', views.booking),
    path('academy', views.academy),
    path('services', views.services),
    path('contact', views.contact)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)