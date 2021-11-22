from django.contrib.auth.models import User
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import *
from .portfolioApi import get_pct_change
from api.models import *
import time
import requests

def get_positions(positions):
    total = get_pos()
    print(total.keys())
    symbols = {}
    for p in positions:
        symbols[p.symbol]= {
            "id": p.id,
            "pos": p.position,
            "share_pct": float("{:.2f}".format((p.position/total["position__sum"])*100))
        }
    data_symbols = ""
    for p in positions:
        data_symbols += f"{p.symbol}%2C"
    url = f"https://yfapi.net/v6/finance/quote?region=US&lang=en&symbols={data_symbols}"
    url_response = requests.get(url, headers={"x-api-key": "XwS5ojLx0g7uvGoBumUwO4agLnD4RZ085EQbtj73"})
    response = url_response.json()["quoteResponse"]["result"]
    for r in response:
        r["id"] = symbols[r["symbol"]]["id"]
        r["pos"] = symbols[r["symbol"]]["pos"]
        r["share_pct"] = symbols[r["symbol"]]["share_pct"]
    # print("ITEMS", symbols)
    # for s in symbols:
    # response["pos"] = s["pos"]
    # response["share_pct"] = float("{:.2f}".format((s["pos"]/total["position__sum"])*100))
    # response["id"] = s['id']

    return response


def get_pos():
    pos = Positions.objects.aggregate(Sum('position'))
    return pos


class PositionListVew(APIView):
    def get(self, request):
        '''
        :param request:
        :return:
        '''
        positions = Positions.objects.all().order_by('symbol')
        return Response({"error": False,
                         "message": "Positions retrieved.",
                         "data": get_positions(positions)})

