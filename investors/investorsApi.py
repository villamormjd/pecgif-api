from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import UserSerializers, UserProfileSerializers
from api.models import UserProfile
from django.contrib.auth.models import User

class InvestorsView(APIView):

    def get(self, request):
        investors = UserProfile.objects.all()
        serializer = UserProfileSerializers(investors, many=True, context={"request": request})

        return Response({"error": False, "message": "Investors retrieved.",
                         "data": serializer.data})


class InvestorDetailView(APIView):

    def get(self, request, investor_num=None):
        print(investor_num)
        investor = UserProfile.objects.get(investor_num=investor_num)
        serializer = UserProfileSerializers(investor, context={"request": request})

        return Response({"error": False, "message": "Single Investor retrieved.",
                         "data": serializer.data})