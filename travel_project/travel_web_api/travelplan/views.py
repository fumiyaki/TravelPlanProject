import django_filters
from rest_framework import viewsets, filters

from .models import User, TourismSpot, RoutePlan, RoutePlanSpot
from .serializer import UserSerializer, TourismSpotSerializer, RoutePlanSerializer, RoutePlanSpotSerializer

from .decorators import multi_create

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = ('user_id', 'password')


class TourismSpotViewSet(viewsets.ModelViewSet):
    queryset = TourismSpot.objects.all()
    serializer_class = TourismSpotSerializer
    filter_fields = ('id', 'name', 'prefecture')


class RoutePlanViewSet(viewsets.ModelViewSet):
    queryset = RoutePlan.objects.all()
    serializer_class = RoutePlanSerializer
    filter_fields = ('id', 'user', )


class RoutePlanSpotViewSet(viewsets.ModelViewSet):
    queryset = RoutePlanSpot.objects.all()
    serializer_class = RoutePlanSpotSerializer
    filter_fields = ('route_plan', )
    order_by = ('order_num', )

    @multi_create(serializer_class=RoutePlanSpotSerializer)
    def create(self, request):
        print(request)
