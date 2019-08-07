from django.contrib.auth.models import User

from rest_framework import serializers

from core1.models import *
import pylint



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("__all__")

class InvitedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model =  InvitedUser
        fields = ("__all__")
        
class UserInterestedCountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInterestedCountry
        fields = ("__all__")
class PackageTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PackageType
        fields = ("__all__")
        
class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ("__all__")
        
class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ("__all__")
        
class UserTravelerInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserTravelerInfo
        fields = ("__all__")
        
class UserExpeditorInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserExpeditorInfo
        fields = ("__all__")
class PackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Package
        fields = ("__all__")
class BlockUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlockUser
        fields = ("__all__")
        
class ReportUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportUser
        fields = ("__all__")

class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = ("__all__")
class BidSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bid
        fields = ("__all__")
class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ("__all__")
class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ("__all__")
