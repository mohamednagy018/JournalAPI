from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import stock
from .serializeres import stockserializer
from .getData import all_news

# Create your views here.
class StockList (APIView):
    def get(self,request):
        stocks = stock.objects.all()
        serializer = stockserializer (stocks , many=True)
        return Response(serializer.data)

    get_news_dec = {}
    def post(self, request):
        recevied_news = []
        recevied_news = all_news
        for i in range(0, len(recevied_news)):
            get_news_dec = {"news": recevied_news[i]}
            #print(get_dec)
            serializer = stockserializer(data=get_news_dec)
            if serializer.is_valid():
                serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        stocks = stock.objects.all()
        stocks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    """def delete(self,request):

    """

"""
de_data={"name":"hesham", "age":21 }
serializer = stockserializer(data=dec_data)
"""