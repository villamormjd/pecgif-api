from django.contrib import admin
from api.models import *
# Register your models here.

myModels = [UserProfile, UserShare, UserAttribute, Transaction, TransactionType, ShareType,
            Portfolio, Positions, UserType, Notification, FrequentlyAskedQuestion]

admin.site.register(myModels)