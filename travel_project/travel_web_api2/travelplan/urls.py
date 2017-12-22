from rest_framework import routers
from django.conf.urls import url, include
from .views import AuthRegister, AuthInfoGetView, AuthInfoUpdateView, AuthInfoDeleteView, TourismSpotViewSet, RoutePlanViewSet, RoutePlanSpotViewSet


urlpatterns = [
    url(r'^user/register/$', AuthRegister.as_view()),
    url(r'^user/mypage/$', AuthInfoGetView.as_view()),
    url(r'^user/auth_update/$', AuthInfoUpdateView.as_view()),
    url(r'^user/delete/$', AuthInfoDeleteView.as_view()),
]

router = routers.DefaultRouter()
router.register(r'tourismspot', TourismSpotViewSet)
router.register(r'routeplanspot', RoutePlanSpotViewSet)
router.register(r'routeplan', RoutePlanViewSet)
urlpatterns += router.urls
