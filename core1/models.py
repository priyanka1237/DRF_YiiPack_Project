from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext, ugettext_lazy as _
from django.utils.timezone import utc
import datetime
# Create your models here.


PHONE_STATUS_UNVERIFIED = 'phone_status_unverified'
PHONE_STATUS_VERIFIED = 'phone_status_verified'
PHONE_STATUS_CHOICES = (
    (PHONE_STATUS_UNVERIFIED, _('g_phone_status_unverified')),
    (PHONE_STATUS_VERIFIED, _('g_phone_status_verified')),
)

LOGIN_TYPE_STATUS_EMAIL = 'login_type_status_email'
LOGIN_TYPE_STATUS_FACEBOOK = 'login_type_status_facebook'
LOGIN_TYPE_STATUS_GOOGLE = 'login_type_status_google'
LOGIN_TYPE_STATUS_CHOICES = (
    (LOGIN_TYPE_STATUS_EMAIL, _('g_login_type_status_email')),
    (LOGIN_TYPE_STATUS_FACEBOOK, _('g_login_type_status_facebook')),
    (LOGIN_TYPE_STATUS_GOOGLE, _('g_login_type_status_google')),
)

PACKAGE_STATUS_PENDING = 'package_status_pending'
PACKAGE_STATUS_ASSIGNED = 'package_status_assigned'
PACKAGE_STATUS_CANCELLED = 'package_status_cancelled'
PACKAGE_STATUS_CHOICES = (
    (PACKAGE_STATUS_PENDING, _('g_package_status_pending')),
    (PACKAGE_STATUS_ASSIGNED, _('g_package_status_assigned')),
    (PACKAGE_STATUS_CANCELLED, _('g_package_status_cancelled')),
)

PACKAGE_INVITATION_STATUS_PENDING = 'package_invitation_status_pending'
PACKAGE_INVITATION_STATUS_ACCEPTED = 'package_invitation_status_accepted'
PACKAGE_INVITATION_STATUS_CANCELLED = 'package_invitation_status_cancelled'
PACKAGE_INVITATION_STATUS_CANCELLED_BY_OWN = 'package_invitation_status_cancelled_by_own'
PACKAGE_INVITATION_STATUS_CHOICES = (
    (PACKAGE_INVITATION_STATUS_PENDING, _('g_package_invitation_status_pending')),
    (PACKAGE_INVITATION_STATUS_ACCEPTED, _('g_package_invitation_status_accepted')),
    (PACKAGE_INVITATION_STATUS_CANCELLED, _('g_package_invitation_status_cancelled')),
    (PACKAGE_INVITATION_STATUS_CANCELLED_BY_OWN, _('g_package_invitation_status_cancelled_by_own')),
)

BID_STATUS_PENDING = 'bid_status_pending'
BID_STATUS_ACCEPTED = 'bid_status_accepted'
BID_STATUS_CANCELLED = 'bid_status_cancelled'
BID_STATUS_CANCELLED_BY_OWN = 'bid_status_cancelled_by_own'
BID_STATUS_CHOICES = (
    (BID_STATUS_PENDING, _('g_bid_status_pending')),
    (BID_STATUS_ACCEPTED, _('g_bid_status_accepted')),
    (BID_STATUS_CANCELLED, _('g_bid_status_cancelled')),
    (BID_STATUS_CANCELLED_BY_OWN, _('g_bid_status_cancelled_by_own')),
)

class User(AbstractUser):
    email= models.CharField(max_length=255,null=True,blank=True,default='')
    first_name= models.CharField(max_length=255,null=True,blank=True)
    last_name= models.CharField(max_length=255,null=True,blank=True)
    password= models.CharField(max_length=255,null=True,blank=True)

    pass
    id = models.BigAutoField(primary_key=True)
    date_of_birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True)
    phone_status = models.CharField(max_length=64, choices=PHONE_STATUS_CHOICES)
    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    image = models.CharField(max_length=255, default="")
    login_status = models.CharField(max_length=64, choices=LOGIN_TYPE_STATUS_CHOICES)
    socialId = models.CharField(max_length=255, default="")
    rating = models.DecimalField(default=0,max_digits=12,decimal_places=3)
    created_time = models.DateTimeField()
    role = models.IntegerField(default=-1)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        super(User, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _('model_auth_user')
        verbose_name_plural = _('model_auth_users')
        db_table = 'auth_user'
        
class InvitedUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=15, blank=True)
    invitation_time = models.DateTimeField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.invitation_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        super(InvitedUser, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _('model_invited_user')
        verbose_name_plural = _('model_invited_users')
        db_table = 'invited_user'

class UserInterestedCountry(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _('model_user_interested_country')
        verbose_name_plural = _('model_user_interested_countries')
        db_table = 'user_interested_country'
        
class PackageType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    
    class Meta:
        verbose_name = _('model_package_type')
        verbose_name_plural = _('model_package_types')
        db_table = 'user_package_type'
    
class UserTravelerInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    no_of_times_travel = models.IntegerField(default=0)
    package_type = models.ForeignKey(PackageType, null=True, blank=True, on_delete=models.CASCADE)
    when_to_travel = models.CharField(max_length=10, blank=True)
    
    class Meta:
        verbose_name = _('model_user_traveler_info')
        verbose_name_plural = _('model_user_traveler_infos')
        db_table = 'user_traveler_info'
        
class UserExpeditorInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    no_of_times_travel = models.IntegerField(default=0)
    package_type = models.ForeignKey(PackageType, null=True, blank=True, on_delete=models.CASCADE)
    when_to_send = models.CharField(max_length=10, blank=True)
    
    class Meta:
        verbose_name = _('model_user_expeditor_info')
        verbose_name_plural = _('model_user_expeditor_infos')
        db_table = 'user_expeditor_info'
    
class Package(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    package_status = models.CharField(max_length=64, choices=PACKAGE_STATUS_CHOICES)
    package_type = models.ForeignKey(PackageType, null=True, blank=True, on_delete=models.CASCADE)
    departure_country = models.CharField(max_length=100, blank=True)
    departure_city = models.CharField(max_length=100, blank=True)
    departure_address = models.CharField(max_length=255, blank=True)
    arrival_country = models.CharField(max_length=100, blank=True)
    arrival_city = models.CharField(max_length=100, blank=True)
    arrival_address = models.CharField(max_length=255, blank=True)
    
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    package_name = models.CharField(max_length=150, blank=True)
    
    width = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    length = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    description_info = models.TextField(default='')
    
    receiver_name = models.CharField(max_length=150, blank=True)
    receiver_email = models.EmailField(max_length=255, unique=True)
    receiver_phone = models.CharField(max_length=15, blank=True)
    receiver_address = models.CharField(max_length=255, blank=True)
    
    urgent_announcement = models.BooleanField(default=False)
    no_of_days = models.IntegerField(default=0)
    inform_to_receiver = models.BooleanField(default=False)
    
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        super(Package, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _('model_package')
        verbose_name_plural = _('model_packages')
        db_table = 'package'
        
class Trip(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
    departure_country = models.CharField(max_length=100, blank=True)
    departure_city = models.CharField(max_length=100, blank=True)
    departure_address = models.CharField(max_length=255, blank=True)
    arrival_country = models.CharField(max_length=100, blank=True)
    arrival_city = models.CharField(max_length=100, blank=True)
    arrival_address = models.CharField(max_length=255, blank=True)
    
    departure_time = models.DateTimeField(blank=True, null=True)
    return_time = models.DateTimeField(blank=True, null=True)
    package_name = models.CharField(max_length=150, blank=True)
    
    width = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    length = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    flight_info = models.TextField(default='')
    
    is_your_travel_urgent = models.BooleanField(default=True)
    created_time = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        super(Trip, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _('model_trip')
        verbose_name_plural = _('model_trips')
        db_table = 'trip'
        
class BlockUser(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="blocked_to")
    blocked_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="blocked_by")
    block_time = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.block_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        super(BlockUser, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _('model_block_user')
        verbose_name_plural = _('model_block_users')
        db_table = 'block_user'
        
class ReportUser(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="reported_to")
    reported_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="reported_by")
    report_time = models.DateTimeField()
    reason = models.CharField(max_length=100, blank=True)
    other_info = models.TextField(default='')
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.report_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        super(ReportUser, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _('model_report_user')
        verbose_name_plural = _('model_report_users')
        db_table = 'report_user'
        
class Message(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    sender = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="receiver")
    message_time = models.DateTimeField()
    message = models.TextField(default='')
    is_read = models.BooleanField(default=False)
    sender_status = models.BooleanField(default=True)
    receiver_status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = _('model_message')
        verbose_name_plural = _('model_messages')
        db_table = 'message'
        
class ContactUs(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField(default='')
    created_time = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        super(ContactUs, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _('model_contact_us')
        verbose_name_plural = _('model_contact_us')
        db_table = 'contact_us'
        
class PackageInvitation(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, null=True, blank=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    package_invitation_status = models.CharField(max_length=64, choices=PACKAGE_INVITATION_STATUS_CHOICES)
    created_time = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        super(PackageInvitation, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _('model_package_invitation')
        verbose_name_plural = _('model_package_invitations')
        db_table = 'package_invitation'
        
class Bid(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, null=True, blank=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    from_time = models.DateTimeField(blank=True, null=True)
    to_time = models.DateTimeField(blank=True, null=True)
    bid_status = models.CharField(max_length=64, choices=BID_STATUS_CHOICES)
    created_time = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        super(Bid, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _('model_bid')
        verbose_name_plural = _('model_bids')
        db_table = 'bid'
        
class Transaction(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, null=True, blank=True, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=150, blank=True)
    created_time = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        super(Transaction, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _('model_transaction')
        verbose_name_plural = _('model_transactions')
        db_table = 'transaction'
        
class Rating(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="rating_to")
    rating_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="rating_by")
    package = models.ForeignKey(Package, null=True, blank=True, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=2, null=True)
    comment = models.TextField(default='')
    created_time = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        super(Rating, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _('model_rating')
        verbose_name_plural = _('model_ratings')
        db_table = 'rating'

class Notification(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    sender = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="notification_sender")
    receiver = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="notification_receiver")
    notification_time = models.DateTimeField()
    message = models.TextField(default='')
    is_read = models.BooleanField(default=False)
    tag = models.CharField(max_length=150, blank=True)
    table_id = models.CharField(max_length=150, blank=True)
    
    class Meta:
        verbose_name = _('model_notification')
        verbose_name_plural = _('model_notifications')
        db_table = 'notification'
        
        
        
    



