from django.db import transaction
from django.http import Http404

import django_filters

from rest_framework import viewsets, filters, status
from rest_framework import permissions, generics
from rest_framework.response import Response

from .models import AuthUser, TourismSpot, RoutePlan, RoutePlanSpot
from .serializer import AuthUserSerializer, TourismSpotSerializer, RoutePlanSerializer, RoutePlanSpotSerializer

from .decorators import multi_create

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     filter_fields = ('user_id', 'password')

# ユーザ作成のView(POST)
class AuthRegister(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer

    @transaction.atomic
    def post(self, request, format=None):
        serializer = AuthUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ユーザ情報取得のView(GET)
class AuthInfoGetView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer

    def get(self, request, format=None):
        return Response(data={
            'username': request.user.username,
            'email': request.user.email,
            'profile': request.user.profile,
            'birthday': request.user.birthday,
            'gender': request.user.gender,
            'start_date': request.user.start_date,
            'end_date': request.user.end_date,
            },
            status=status.HTTP_200_OK)

# ユーザ情報更新のView(PUT)
class AuthInfoUpdateView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AuthUserSerializer
    lookup_field = 'email'
    queryset = AuthUser.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(email=self.request.user)
            return instance
        except AuthUser.DoesNotExist:
            raise Http404

# ユーザ削除のView(DELETE)
class AuthInfoDeleteView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AuthUserSerializer
    lookup_field = 'email'
    queryset = AuthUser.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(email=self.request.user)
            return instance
        except AuthUser.DoesNotExist:
            raise Http404


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
