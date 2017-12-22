from rest_framework import serializers

from .models import AuthUser, TourismSpot, RoutePlanSpot, RoutePlan


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('user_id', 'password', 'name', 'gender', 'address')
        # fields = ('user_id', 'password', 'name', 'mail', 'phone_num', 'birthday', 'gender', 'authority', 'start_date', 'end_date', 'address', 'user_entry_date')


class AuthUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = AuthUser
        fields = ('id', 'username', 'email', 'profile', 'password', 'birthday', 'gender', 'start_date', 'end_date')

    def create(self, validated_data):
        return AuthUser.objects.create_user(request_data=validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        else:
            instance = super().update(instance, validated_data)
        instance.save()
        return instance


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
