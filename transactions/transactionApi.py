from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import UserProfile, Transaction, TransactionType, UserAttribute
from api.serializers import TransactionSerializers, TransactionTypeSerializers
from utils.utils import generate_string
from django.db.models import Sum


class UserTransactionsView(APIView):

    def post(self, request, investor_number=None):
        '''
        :param request: investor, date, amount, type - 12, 13
        :return:
        '''
        print(request.data)
        amount = request.data["amount"]
        transaction_type = request.data["type"]

        up = UserProfile.objects.get(investor_num=investor_number)
        transaction = Transaction.objects.create(
            user=up.user,
            transaction_number=generate_string(),
            amount=float(amount),
            type=TransactionType.objects.get(pk=transaction_type)
        )

        if transaction:
            original_investment, created = UserAttribute.objects.get_or_create(name="original_investment", user=transaction.user)
            total_investment, created = UserAttribute.objects.get_or_create(name="total_investment", user=transaction.user,
                                                                            user_transaction=transaction)
            top_ups = Transaction.objects.filter(user=up.user, type=12).aggregate(top_ups=Sum('amount'))["top_ups"] or 0.00
            withdraws = Transaction.objects.filter(user=up.user, type=13).aggregate(withdraws=Sum('amount'))["withdraws"] or 0.00
            total = float(original_investment.value) + (float(top_ups)-float(withdraws))
            total_investment.value = "{:.2f}".format(total)
            total_investment.save()
        serializers = TransactionSerializers(transaction, context={"request": request})
        return Response({"error": False, "message": "Transaction have been saved.",
                         "data": serializers.data}, status=status.HTTP_200_OK)

    def get(self, request, investor_num=None):
        print("TRANSACTIONS", investor_num)
        try:
            up = UserProfile.objects.get(investor_num=investor_num)
            transactions = Transaction.objects.filter(user=up.user).order_by('-id')
            serializers = TransactionSerializers(transactions, many=True, context={"request": request})
            return Response({"error": False, "message": "User transactions retrieved.",
                             "data": serializers.data}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
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