from rest_framework import routers
from .views import UserViewSet, TourismSpotViewSet, RoutePlanViewSet, RoutePlanSpotViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tourismspot', TourismSpotViewSet)
router.register(r'routeplanspot', RoutePlanSpotViewSet)
router.register(r'routeplan', RoutePlanViewSet)
