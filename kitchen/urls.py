from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mom.urls')),
    path('customer/',include('customer.urls')),
    path('register/',include('validations.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
