from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),   # ✅ Admin section
    path('api/', include('accounts.urls')),
]
