from django.contrib import admin
from api.models import *
# Register your models here.

myModels = [UserProfile, UserShare, UserAttribute, Transaction, TransactionType, ShareType,
            Portfolio, Positions, UserType, Notification]

admin.site.register(myModels)