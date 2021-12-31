from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import *
from api.models import *
import time

def get_pct_change(original, new):
    '''
    :param original: previous
    :param new: current
    :return: pct change

    original > new - decrease
    original < new - increase
    '''
    print("OR",original)
    if original == 0:
        return 0

    if (original > new):
        pct = -((original - new)/original)*100
    elif (original < new):
        pct = ((new - original)/original)*100

    return float("{:.2f}".format(pct))

def get_nlv_analytics(portfolios):
    anlytics=[]
    for p in portfolios:
        date = p.created_on.strftime("%B %d")
        print(date)
        anlytics.append({"date": date,
                         "nlv": p.nlv,
                         "pos": p.total_positions})

    return anlytics


class PortfolioListView(APIView):

    def get(self, request):
        '''
        :param request:
        :return:
        '''

        portfolios = Portfolio.objects.all().order_by('created_on')
        serializers = PortfolioSerializers(portfolios,many=True, context={"request": request})
        print(list(portfolios)[-1], list(portfolios)[-2])
        previous = list(portfolios)[-2]
        current = list(portfolios)[-1]
        pct_nlv = get_pct_change(previous.nlv, current.nlv)
        #print("NLV",pct_nlv)
        pct_buying_power = get_pct_change(previous.buying_power, current.buying_power)
        #print("PWr", pct_buying_power)
        pct_total_positions = get_pct_change(previous.total_positions, current.total_positions)
       # print("POS", pct_total_positions)
        return Response({"error": False, "message": "Portfolio retrieved.",
                         "data": serializers.data[-1],
                         "nlv_pct": pct_nlv,
                         "pwr_pct": pct_buying_power,
                         "pos_pct": pct_total_positions,
                         "nlv_analytics": get_nlv_analytics(portfolios)})