from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from content.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
]

# /media/product.png,
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# /static/hello.js
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
