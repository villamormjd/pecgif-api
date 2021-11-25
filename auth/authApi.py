from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import *
from api.models import *
from utils.utils import mask_email, generate_code
from utils.services import email_generated_code, email_activation
import time, datetime


def generate_username():
    print(2)
    latest_id = User.objects.latest('id').id
    print(latest_id, type(latest_id))
    next_user_id = int(latest_id) + 1
    username = "pecgif0{}".format(next_user_id)
    print("USERNAME", username)
    return username

class LoginView(APIView):
    def post(self, request):
        '''
        :param request: username, password
        :return: user and userprofile data
        '''
        time.sleep(3)
        print(request.data)
        username = request.data["username"]
        password = request.data["password"]

        user = User.objects.filter(username=username).first()
        if user is None:
            return Response({"error": True,
                             "message": "We don't recognize user with that username."})

        if not user.is_active:
            return Response({"error": True,
                             "message": "This user is not active."})

        if not user.check_password(password):
            return Response({"error": True,
                             "message": "Password is incorrect"})

        print(user.username)
        if user.is_superuser:
            serializer = UserSerializers(user, context={"request": request})

            return Response({"error": False,
                             "message": "Login Successful",
                             "data": serializer.data})
        else:
            up = UserProfile.objects.get(user=user)
            if not up:
                return Response({"error": True,
                                 "message": "We cannot find this account"})
            serializer = UserSerializers(user, context={"request": request})

            return Response({"error": False,
                             "message": "Login Successful",
                             "data": serializer.data})


class RegisterView(APIView):
    def post(self, request):
        print(request.data)
        if request.data:
            print(1)
            try:
                user = User.objects.create(
                    first_name=request.data["first_name"],
                    last_name=request.data["last_name"],
                    email=request.data["email"],
                    username=generate_username(),
                    date_joined=datetime.datetime.strptime(request.data["date_joined"], '%m/%d/%y'),
                    is_active=False)
                print("USER", user)
                if user:
                    up = UserProfile.objects.create(
                        user=user,
                        investor_num=request.data["investor_num"],
                        control_num=request.data["control_num"],
                        cell_phone_num=request.data["cell_phone_num"],
                        bank_account_number=request.data["account_num"],
                        bank_account_name=request.data["bank"],
                        bank_account_currency=request.data["currency"],
                        user_type=UserType.objects.get(name="Investor")
                    )

                    orinigal_investment = UserAttribute.objects.create(
                        user=user, name="original_investment", value=request.data["original_investment"]
                    )
                    total_investment = UserAttribute.objects.create(user=user, name="total_investment",
                                                                    value=orinigal_investment.value)
                    user_share = UserShare.objects.create(user=user,
                                                          total_share=int(request.data["total_share"]),
                                                          share_type=ShareType.objects.get(name=request.data["share_type"]))
                    serializer = UserSerializers(user, context={"request": request})
                    return Response({"error": False,
                                     "message": "Investor created",
                                     "data": serializer.data})
            except Exception as e:
                return Response({"error": True,
                                 "message": "Investor failed to create",
                                 "error": str(e)})


class EditUserView(APIView):

    def put(self, request):
        '''
        :param request: email, investor_num, control_num, cell_phone_num, original_investment, share, share_type
        :return:
        '''
        params = request.data
        print(request.data)
        up = UserProfile.objects.get(investor_num=params.get('investor_num'))
        user = up.user
        share = UserShare.objects.get(user=user)
        try:
            if params.get('email'):
                user.email = params.get('email')
            if params.get('control_num'):
                up.control_num = params.get('control_num')
            if params.get('cell_phone_num'):
                up.cell_phone_num = params.get('cell_phone_num')
            if params.get('original_investment'):
                orig_inv = UserAttribute.objects.get(user=user, name="original_investment")
                orig_inv.value = params.get('original_investment')
                orig_inv.save()
            if params.get('total_share'):
                share.total_share = params.get('total_share')
            if params.get('share_type'):
                share.share_type = ShareType.objects.get(name=params.get('share_type'))
            if params.get('account_num'):
                up.bank_account_number = params.get('account_num')
            if params.get('bank'):
                up.bank_account_name = params.get('bank')
            if params.get('currency'):
                up.bank_account_currency = params.get('currency')

            up.save()
            user.save()
            share.save()
            serializer = UserSerializers(user, context={"request": request})

            return Response({"error": False, "message": "Investor updated successfully",
                             "data": serializer.data})
        except Exception as e:
            return Response({"error": True, "message": "Failed to update investor",
                             "error_message": str(e)})


class ActivateAccount(APIView):
    '''
    request: investor_num, username, password
    '''
    def post(self, request):
        investor_num = request.data["investor_num"]
        try:
            up = UserProfile.objects.get(investor_num=investor_num)

            if up.has_activated:
                return Response({"error": True, "message": "Account with that investor number already activated."})

            user = up.user
            email = mask_email(user.email)
            up.activation_code = generate_code()
            up.save()
            email_generated_code(up.activation_code, user.email)
            return Response({"error": False, "message": "We've sent confirmation code to {}".format(email),
                             "email": email})
        except Exception as e:
            print(e)
            return Response({"error": True, "message": "Investor Number not found"})


class VerifyActivateCode(APIView):
    def post(self, request):
        up = UserProfile.objects.get(investor_num=request.data["investor_num"])
        if up.activation_code != request.data["code"]:
            return Response({"error": True, "message": "Verification code invalid."})

        user = up.user
        user.is_active = True
        user.set_password(request.data["password"])
        up.has_activated = True
        up.save()
        user.save()
        email_activation(user, up)
        return Response({"error": False, "message": "Activation Success. You may now login."})

# {
# "cell_phone_num": "123456789",
# "control_num": "2020-001",
# "date_joined": "10/27/2021",
# "email": "villamormjd@gmail.com",
# "first_name": "Jason",
# "investor_num": "987654",
# "last_name": "Villamor",
# "original_investment": "5000"}

# {
# "cell_phone_num": "123456789",
# "control_num": "2020-001",
# "email": "villamormjd@gmail.com",
# "investor_num": "987654",
# "original_investment": "5000",
# "share_type": "PS",
# "total_share": "200"}