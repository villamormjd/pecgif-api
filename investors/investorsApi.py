from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import UserSerializers, UserProfileSerializers
from api.models import UserProfile, UserType
from django.contrib.auth.models import User

class InvestorsView(APIView):

    def get(self, request):
        user_type = UserType.objects.get(pk=2)
        investors = UserProfile.objects.filter(user_type=user_type, is_active=True).order_by('investor_num')
        serializer = UserProfileSerializers(investors, many=True, context={"request": request})

        return Response({"error": False, "message": "Investors retrieved.",
                         "data": serializer.data})


class InvestorDetailView(APIView):

    def get(self, request, investor_num=None):
        investor = UserProfile.objects.get(investor_num=investor_num)
        serializer = UserProfileSerializers(investor, context={"request": request})

        return Response({"error": False, "message": "Single Investor retrieved.",
                         "data": serializer.data})