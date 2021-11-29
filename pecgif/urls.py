"""pecgif URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from auth.authApi import *
from investors.investorsApi import InvestorsView, InvestorDetailView
from portfolio.portfolioApi import *
from portfolio.positionsApi import PositionListVew
from transactions.transactionApi import UserTransactionsView, TransactionsListView, TransactionsTypeListView
from notifications.notificationApi import NotificationView

urlpatterns = [
    path('admin/', admin.site.urls),

    #auth API
    path('api/v1/login/', LoginView.as_view(), name="login"),
    path('api/v1/user/create/', RegisterView.as_view(), name="create-user"),
    path('api/v1/user/edit/', EditUserView.as_view(), name="edit-user"),
    path('api/v1/portfolio/', PortfolioListView.as_view(), name="portfolio"),
    path('api/v1/positions/', PositionListVew.as_view(), name="positions"),
    path('api/v1/user/<int:investor_num>/transactions/lists/', UserTransactionsView.as_view(), name="user-transactions"),
    path('api/v1/transactions/lists/', TransactionsListView.as_view(), name="lists-transactions"),
    path('api/v1/transactions-type/lists/', TransactionsTypeListView.as_view(), name="lists-transactions"),
    path('api/v1/user/transactions/create/', UserTransactionsView.as_view(), name="transaction-create"),
    path('api/v1/investors/lists/', InvestorsView.as_view(), name="investors-lists"),
    path('api/v1/investors/<int:investor_num>/single/', InvestorDetailView.as_view(), name="investors-single"),
    path('api/v1/user/activate/', ActivateAccount.as_view(), name="activate-account"),
    path('api/v1/user/verify/', VerifyActivateCode.as_view(), name="verify-account"),
    path('api/v1/notifications/', NotificationView.as_view(), name="notifications"),

]
