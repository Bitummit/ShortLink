from django.contrib import admin
from django.urls import path, include
from link import services

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('link.urls')),
    # path('<str:short_url>', services.redirect_short),
]
