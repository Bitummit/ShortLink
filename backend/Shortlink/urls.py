from django.contrib import admin
from django.urls import path, include
from link import redirection

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('link.urls')),
    path('<str:short_link>/', redirection.redirect_short),
]
