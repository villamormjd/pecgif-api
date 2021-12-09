from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import *
from api.models import *


class NotificationView(APIView):

     def get(self, request):
         notifications = Notification.objects.all().order_by('-created_on')
         serializers = NotificatioSerializers(notifications, many=True, context={"request": request})
         unread = Notification.objects.filter(is_read=False).count()
         return Response({"error": False, "message": "Notifications retrieved.", "unread": unread,
                          "data": serializers.data})

     def post(self, request):
         '''
         :param request: investor_num, message
         :return:
         '''
         investor_num = request.data["investor_num"]
         message = request.data["message"]
         try:
             up = UserProfile.objects.get(investor_num=investor_num)
             notification = Notification.objects.create(user=up.user, notification_message=message)
             print("MESSAGE", message)
             return Response({"error": False, "message": "Your inquiry has been sent.".format(message)})
         except Exception as e:
             return Response({"error": True, "message": "Something went wrong. {}".format(e)})
