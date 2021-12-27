from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # path('repos/', include('checkingGitStatus.urls')),
    path('', include('checkingGitStatus.urls')),
]

