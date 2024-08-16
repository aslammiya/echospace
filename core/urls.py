from django.contrib import admin
from django.urls import path
from home.views import *
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('check_username/', check_username, name='check_username'),
    path('login/', sign_in, name='login'),
    path('saveProfileInfo/', saveProfileInfo, name='saveProfileInfo'),
    path('check_old_password/', check_old_password, name='check_old_password'),
    path('guest_login/', guest_login, name='guest_login'),
    path('logout/', sign_out, name='logout'),
    path('changePassword/', changePassword, name='changePassword'),
    path('register/', sign_up, name='register'),
    path('room/<str:roomname>/<str:status>/', createRoom, name='createRoom'),
    path('leave/<str:roomname>/', leaveRoom, name="leaveRoom"),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', home, name="home"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)