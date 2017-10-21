from rest_framework import serializers

from .models import User, TourismSpot, RoutePlanSpot, RoutePlan


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'password', 'name', 'gender', 'address')
        # fields = ('user_id', 'password', 'name', 'mail', 'phone_num', 'birthday', 'gender', 'authority', 'start_date', 'end_date', 'address', 'user_entry_date')


class TourismSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourismSpot
        fields = ('id', 'name', 'desc', 'prefecture', 'address', 'phone_num', 'parkinglot', 'holiday', 'business_hours', 'charge', 'coordinate_latitude', 'coordinate_longitude', 'grade')


class RoutePlanSerializer(serializers.ModelSerializer):
    # route_plan_spot = RoutePlanSpotSerializer(many=True)
    # route_plan_spot = RoutePlanSpotSerializer()

    class Meta:
        model = RoutePlan
        fields = ('id', 'name', 'desc', 'user')


class RoutePlanSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutePlanSpot
        fields = ('route_plan', 'spot', 'order_num', 'start_time', 'finish_time')
