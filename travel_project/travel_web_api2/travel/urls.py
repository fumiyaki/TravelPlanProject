from django.conf.urls import url, include
from django.contrib import admin

from travelplan.urls import router

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', obtain_jwt_token),
    url(r'^token-refresh/', refresh_jwt_token),
    url(r'^token-verify/', verify_jwt_token),
    url(r'^api/', include('travelplan.urls')),
]
