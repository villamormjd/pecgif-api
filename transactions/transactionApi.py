from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import UserProfile, Transaction, TransactionType, UserAttribute, UserShare
from api.serializers import TransactionSerializers, TransactionTypeSerializers
from utils.utils import generate_string
from django.db.models import Sum
from datetime import datetime

def create_user_attribute(transaction, user):
    if transaction:
        original_investment, created = UserAttribute.objects.get_or_create(name="original_investment",
                                                                           user=transaction.user)
        if transaction.type.name == "New Principal":
            original_investment.value = transaction.amount
            original_investment.save()
        total_investment, created = UserAttribute.objects.get_or_create(name="total_investment", user=transaction.user,
                                                                        user_transaction=transaction)
        top_ups = Transaction.objects.filter(user=user, type__name="Top-up").aggregate(top_ups=Sum('amount'))[
                      "top_ups"] or 0.00
        withdraws = \
        Transaction.objects.filter(user=user, type__name="Withdrawal").aggregate(withdraws=Sum('amount'))[
            "withdraws"] or 0.00
        total = float(original_investment.value) + (float(top_ups) - float(withdraws))
        total_investment.value = "{:.2f}".format(total)
        total_investment.save()

class UserTransactionsView(APIView):

    def post(self, request):
        '''
        :param request: investor, date, amount, type
        :return:
        '''
        transaction_type = TransactionType.objects.get(pk=request.data["type"])
        amount = request.data["amount"]
        trans_date = datetime.strptime(request.data["date"], "%m/%d/%Y")

        if transaction_type.name.upper() == "DIVIDENDS":
           investors = UserProfile.objects.filter(user_type_id=2)
           users = [i.user for i in investors]
           for u in users:
               user_share = UserShare.objects.filter(user=u)
               shares = user_share.aggregate(total_shares=Sum("total_share"))["total_shares"]
               dividends = shares * float(amount)
               transaction = Transaction.objects.create(
                   user=u,
                   transaction_number=generate_string(),
                   amount=dividends,
                   type=transaction_type,
                   date=trans_date
               )
               create_user_attribute(transaction, u)
           return Response({"error": False, "message": "Dividends Transactions saved."})
        elif transaction_type.name.upper() == "NEW PRINCIPAL":
            investor_number = request.data["investor"]
            up = UserProfile.objects.get(investor_num=investor_number)
            transaction = Transaction.objects.create(
                user=up.user,
                transaction_number=generate_string(),
                amount=float(amount),
                type=transaction_type,
                date=trans_date
            )
            create_user_attribute(transaction, up.user)
            serializers = TransactionSerializers(transaction, context={"request": request})
            return Response({"error": False, "message": "Transaction have been saved.",
                             "data": serializers.data}, status=status.HTTP_200_OK)
        else:
            investor_number = request.data["investor"]
            up = UserProfile.objects.get(investor_num=investor_number)
            transaction = Transaction.objects.create(
                user=up.user,
                transaction_number=generate_string(),
                amount=float(amount),
                type=transaction_type,
                date=trans_date
                )
            create_user_attribute(transaction, up.user)
            serializers = TransactionSerializers(transaction, context={"request": request})
            return Response({"error": False, "message": "Transaction have been saved.",
                             "data": serializers.data}, status=status.HTTP_200_OK)

    def get(self, request, investor_num=None):
        try:
            up = UserProfile.objects.get(investor_num=investor_num)
            transactions = Transaction.objects.filter(user=up.user).order_by('-id')
            serializers = TransactionSerializers(transactions, many=True, context={"request": request})
            return Response({"error": False, "message": "User transactions retrieved.",
                             "data": serializers.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": True, "message": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)


class TransactionsListView(APIView):

    def post(self, request):
        '''
        :param request: investor, transaction_type, amount, date
        :return:
        '''
        up = UserProfile.objects.get(investor_num=request.data["investor"])
        trans_type = TransactionType.objects.get(pk=int(request.data["transaction_type"]))

    def get(self, request):
        transactions = Transaction.objects.all()
        serializers = TransactionSerializers(transactions, many=True, context={"request": request})
        return Response({"error": False, "message": "User transactions retrieved.",
                             "data": serializers.data}, status=status.HTTP_200_OK)


class TransactionsTypeListView(APIView):

    def get(self, request):

        trans_types = TransactionType.objects.all()
        serializers = TransactionTypeSerializers(trans_types, many=True, context={"request": request})
        return Response({"error": False, "messgae": "Transactions Type list",
                        "data": serializers.data}, status=status.HTTP_200_OK)