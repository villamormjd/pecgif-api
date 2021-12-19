from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from api.serializers import *
from api.models import *


class FrequentlyAskedQuestionsView(APIView):
    def get(self, request):

        faqs = FrequentlyAskedQuestion.objects.all()
        serializers = faqsSerializers(faqs, many=True, context={"request": request})
        return Response({"error": False,
                         "message": "Frequently Asked Questions retrieved.",
                         "data": serializers.data},
                        status=status.HTTP_200_OK)