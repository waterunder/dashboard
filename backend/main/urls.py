from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Django admin
    path("dj-admin/", admin.site.urls),
    # User management
    path("accounts/", include("allauth.urls")),
    # Local apps
    path("", include("dashboard.urls")),
    path("pages/", include("pages.urls")),
    path("products/", include("products.urls")),
    path("sellers/", include("sellers.urls")),
    path("dive/", include("dive.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
