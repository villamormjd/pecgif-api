from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import *
import datetime
from django.db.models import Sum

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

        extra_kwargs = {
            'password': {'write_only': True},
            'groups': {'write_only': True},
            'user_permissions': {'write_only': True},
        }

    def to_representation(self, instance):
        up = UserProfile.objects.get(user=instance)
        response = super().to_representation(instance)
        response["profile"] = UserProfileSerializers(up).data
        return response


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        user = User.objects.get(id=instance.user.id)
        if user.is_superuser:
            return response
        user_shares = UserShare.objects.filter(user=user)
        shares = user_shares.aggregate(total_shares=Sum("total_share"))["total_shares"]
        ps_share = user_shares.get(share_type_id=4)
        ms_share = None
        if user.is_staff:
            ms_share = user_shares.get(share_type_id=5)
        total_investment = UserAttribute.objects.filter(name="total_investment", user=user).last()
        original_investment = UserAttribute.objects.get(name="original_investment", user=user)
        response["id"] = instance.investor_num
        response["is_staff"] = user.is_staff
        response["is_active"] = "Active" if user.is_active else "Not Active"
        response["email"] = user.email
        response["date_joined"] = user.date_joined.strftime("%m/%d/%Y")
        response["name"] = f"{user.first_name} {user.last_name}"
        response["share"] = shares
        response["share_type"] = "PS, MS" if user.is_staff else "PS"
        response["ps_share"] = ps_share.total_share
        response["ps_type"] = ps_share.share_type.name
        response["ms_share"] = ms_share.total_share if ms_share else None
        response["ms_type"] = ms_share.share_type.name if ms_share else None
        response["total_investment"] = "${:,.2f}".format(float(total_investment.value)) if total_investment.value else 0.00
        response["original_investment"] = "${:,.2f}".format(float(original_investment.value))
        return response



class PortfolioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = "__all__"


class TransactionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

    def to_representation(self, instance):
        trans_type = TransactionType.objects.get(pk=instance.type)
        print(trans_type)
        total_investment = UserAttribute.objects.get(name="total_investment", user=instance.user, user_transaction=instance)
        original_investment = UserAttribute.objects.get(name="original_investment", user=instance.user)


        response = super().to_representation(instance)
        response["transaction_type"] = trans_type.name
        response["original_investment"] = "${:,.2f}".format(float(original_investment.value))
        response["total_investment"] = "${:,.2f}".format(float(total_investment.value))
        response["amount"] = "${:,.2f}".format(float(instance.amount))
        response["date"] = instance.date.strftime("%m/%d/%Y")
        response["name"] = f"{instance.user.first_name} {instance.user.last_name}"
        return response


class TransactionTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model= TransactionType
        fields = "__all__"


class NotificatioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        up = UserProfile.objects.get(user=instance.user)
        user = up.user
        response["investor_num"] = up.investor_num
        response["name"] = f"{user.first_name} {user.last_name}"
        response["created_date"] = datetime.datetime.strftime(instance.created_on, "%m/%d/%Y")
        response["email"] = user.email
        response["username"] = user.username
        return response


class faqsSerializers(serializers.ModelSerializer):
    class Meta:
        model = FrequentlyAskedQuestion
        fields = "__all__"