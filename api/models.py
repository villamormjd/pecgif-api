import datetime

from django.db import models
from django.contrib.auth.models import User


class AuditModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


class UserType(AuditModel):
    name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class UserProfile(AuditModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    investor_num = models.CharField(max_length=15, blank=True, unique=True)
    control_num = models.CharField(max_length=15, blank=True, unique=True)
    cell_phone_num = models.CharField(max_length=15, blank=True)
    has_activated = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=10, blank=True)
    user_type = models.ForeignKey(UserType, related_name="user_type", on_delete=models.CASCADE,
                                  default=None, null=True)
    bank_account_number = models.CharField(max_length=15, blank=True)
    bank_account_name = models.CharField(max_length=15, blank=True)
    bank_account_currency = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.user}"


class TransactionType(AuditModel):
    name = models.CharField(max_length=20, default=None, blank=True)

    def __str__(self):
        return self.name


class Transaction(AuditModel):
    transaction_number = models.CharField(max_length=10, blank=True)
    user = models.ForeignKey(User, related_name="user_transactions", on_delete=models.CASCADE,
                             default=None, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    type = models.ForeignKey(TransactionType, related_name="transaction_type", on_delete=models.CASCADE,
                             default=None, null=True)
    date = models.DateTimeField(default=datetime.datetime.today(), null=True, blank=True)
    #document_link = models.FileField()

    def __str__(self):
        return f"{self.type} - {self.user}"


class UserAttribute(AuditModel):
    '''
        original_investment,
        total_investment,
    '''
    user = models.ForeignKey(User, related_name="user_attribute", on_delete=models.CASCADE,
                             default=None, null=True)
    name = models.CharField(max_length=20, default=None, blank=True)
    value = models.CharField(max_length=20, default="0", blank=True)
    user_transaction = models.ForeignKey(Transaction, related_name="user_attribute_transactions", on_delete=models.CASCADE,
                                    default=None, null=True)

    def __str__(self):
        return f"{self.name} - {self.user}"


class ShareType(AuditModel):
    name = models.CharField(max_length=20, default=None, blank=True)

    def __str__(self):
        return self.name


class UserShare(AuditModel):
    user = models.ForeignKey(User, related_name="user_shares", on_delete=models.CASCADE,
                             default=None, null=True)
    total_share = models.IntegerField(default=0)
    share_type = models.ForeignKey(ShareType, related_name="user_share_type", on_delete=models.CASCADE,
                                   default=None, null=True)

    def __str__(self):
        return f"{self.user} - {self.share_type}"


class Portfolio(AuditModel):
    nlv = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    buying_power = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_positions = models.IntegerField(default=0)


class Positions(AuditModel):
    symbol = models.CharField(max_length=10, default=None, blank=True)
    position = models.IntegerField(default=0)
    market_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    change_pct = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    share_pct = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = "Positions"

    def __str__(self):
        return self.symbol


class Notification(AuditModel):
    user = models.ForeignKey(User, related_name="notification_user", on_delete=models.CASCADE,
                             default=None, null=True)
    notification_message = models.TextField(blank=True)
    is_read = models.BooleanField(default=False)


class Message(AuditModel):
    user = models.ForeignKey(User, related_name="message_user", on_delete=models.CASCADE,
                             default=None, null=True)
    comment = models.TextField(blank=True)


class FrequentlyAskedQuestion(AuditModel):
    question = models.TextField(blank=True)
    answer = models.TextField(blank=True)

    def __str__(self):
        return self.question


