from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, _user_has_perm
)
from django.utils.translation import ugettext_lazy as _

# class User(models.Model):
#     """user profile - ユーザー情報"""
#     GENDER_SET = (
#         ("man", "男性"),
#         ("woman", "女性"),
#         ("unknown", "その他"),
#     )
#     # AUTHORITY_SET = (
#     #     ("admin", "管理者"),
#     #     ("employee", "社員"),
#     #     ("staff", "アルバイト"),
#     # )
#     user_id = models.CharField(primary_key=True, max_length=30)
#     password = models.CharField(max_length=150)
#     name = models.CharField(max_length=30)
#     # mail = models.EmailField(blank=True, null=True)
#     # phone_num = models.CharField(blank=True, null=True, max_length=15)
#     # birthday = models.DateField(blank=True, null=True)
#     gender = models.CharField(choices=GENDER_SET, max_length=10)
#     # authority = models.CharField(choices=AUTHORITY_SET, max_length=10)
#     # start_date = models.DateField(blank=True, null=True)
#     # end_date = models.DateField(blank=True, null=True)
#     address = models.CharField(max_length=100)
#     user_entry_date = models.DateTimeField(blank=True, null=True, default=timezone.now) #その時の時刻が入る
#
#     def __str__(self):
#         return self.name


class AccountManager(BaseUserManager):
    def create_user(self, request_data, **kwargs):
        now = timezone.now()
        if not request_data['email']:
            raise ValueError('Users must have an email address.')

        if request_data.get('profile'):
            profile = request_data['profile']
        else:
            profile = ""

        user = self.model(
            username=request_data['username'],
            email=self.normalize_email(request_data['email']),
            is_active=True,
            last_login=now,
            date_joined=now,
            profile=profile
        )

        user.set_password(request_data['password'])
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        request_data = {
            'username': username,
            'email': email,
            'password': password
        }
        user = self.create_user(request_data)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        # user.is_superuser = True
        user.save(using=self._db)
        return user


class AuthUser(AbstractBaseUser):
    GENDER_SET = (
        ("man", "男性"),
        ("woman", "女性"),
        ("unknown", "その他"),
    )
    username    = models.CharField(_('username'), max_length=30, unique=True)
    first_name  = models.CharField(_('first name'), max_length=30, blank=True)
    last_name   = models.CharField(_('last name'), max_length=30, blank=True)
    email       = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    profile     = models.CharField(_('profile'), max_length=255, blank=True)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)
    is_admin    = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(choices=GENDER_SET, max_length=10)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def user_has_perm(user, perm, obj):
        return _user_has_perm(user, perm, obj)

    def has_perm(self, perm, obj=None):
        return _user_has_perm(self, perm, obj=obj)

    def has_module_perms(self, app_label):
        return self.is_admin

    def get_short_name(self):
        return self.first_name

    @property
    def is_superuser(self):
        return self.is_admin

    class Meta:
        db_table = 'api_user'
        swappable = 'AUTH_USER_MODEL'


class TourismSpot(models.Model):
    """tourism spot - 観光地情報"""
    name = models.CharField(max_length=40, unique=True) #観光地の名前
    desc = models.CharField(blank=True, null=True, max_length=1000) #観光地の説明
    prefecture =  models.CharField(max_length=9) #都道府県
    address = models.CharField(blank=True, null=True, max_length=80) #観光地の住所
    phone_num = models.CharField(blank=True, null=True, max_length=12) #観光地の電話番号
    parkinglot = models.IntegerField(blank=True, null=True) #駐車可能台数
    holiday = models.CharField(blank=True, null=True, max_length=7) #月〜日を直接入れる
    business_hours = models.CharField(blank=True, null=True, max_length=11) #営業時間 00:00-24:59 例10時30分から19時まで営業なら10:30-19:00
    charge = models.PositiveIntegerField(blank=True, null=True) #入園料など，観光地に入るための料金
    coordinate_latitude = models.FloatField(blank=True, null=True)#座標 緯度
    coordinate_longitude = models.FloatField(blank=True, null=True) #座標 経度
    grade = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)]) #評価

    def __str__(self):
        return self.name


class RoutePlan(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(blank=True, null=True)
    # image = models.CharField(max_length=255)
    user = models.ForeignKey(AuthUser, related_name="user")

    def __str__(self):
        return self.name

class RoutePlanSpot(models.Model):
    route_plan = models.ForeignKey(RoutePlan, related_name="route_plan")
    spot = models.ForeignKey(TourismSpot, related_name="spot")
    order_num = models.IntegerField() #行く順番を示す数値が格納
    start_time = models.TimeField(blank=True, null=True)
    finish_time = models.TimeField(blank=True, null=True)
    def __str__(self):
        return self.spot.name + " in " + self.route_plan.name



# class Entry(models.Model):
#     STATUS_DRAFT = "draft"
#     STATUS_PUBLIC = "public"
#     STATUS_SET = (
#             (STATUS_DRAFT, "下書き"),
#             (STATUS_PUBLIC, "公開中"),
#     )
#     title = models.CharField(max_length=128)
#     body = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT, max_length=8)
#     author = models.ForeignKey(AuthUser, related_name='entries')
