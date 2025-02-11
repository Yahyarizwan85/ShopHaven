from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Yahya Clothes Center Admin page"
admin.site.site_title = "Yahya Clothes Center Admin page"
admin.site.index_title = "Welcome to Yahya Clothes Center"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

