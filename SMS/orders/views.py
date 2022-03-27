from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from orders.controller.controller import Controller
from .serializers import CustomerOrderSerailizer, OrderListSerailizer, OrdersDetailsSerializer
from .models import OrdersDetails, FileDetails
from datetime import datetime
import logging

# Get an instance of a logging
log = logging.getLogger(__name__)


# Create your views here.

class CreateOrder(APIView):
    def post(self,request):
        try:
            if Controller().createOrder(request = request):
                return Response({"error":False,"status_code":200,"message":"Data Inserted"})
            else:
               raise KeyError
        
        except KeyError:
            log.error("Invalid Request Data")
            return Response({"error":True,"status_code":400,"message":"Invalid Request Data"})

        except Exception as e:
            log.error(e)
            return Response({"error":True,"status_code":500,"message":str(e)})


class UpdateOrder(APIView):
    def post(self,request,id):
        try:
            response = OrdersDetails.objects.get(order_id = id)
            serializer = OrdersDetailsSerializer(response,data = request.data)
            if serializer.is_valid():
                serializer.save(modified_by = 1, modified_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                log.info("Data Updated")
                return Response({"error":False,"status_code":200,"message":"Data Updated"})
            else:
                log.error(serializer.errors)
                return Response({"error":True,"status_code":400,"message":serializer.errors})
        
        except KeyError:
            log.error("Invalid Request Data")
            return Response({"error":True,"status_code":400,"message":"Invalid Request Data"})

        except Exception as e:
            log.error(e)
            return Response({"error":True,"status_code":500,"message":str(e)})


class OrderList(APIView):
    def post(self,request):
        try:
            response = OrdersDetails.OrdersDetailsList()
            serializer = OrderListSerailizer(response, many=True)
            log.info("Data Retrived")
            return Response({"error":False,"status_code":200,"data":serializer.data})

        except Exception as e:
            log.error(e)
            return Response({"error":True,"status_code":500,"message":str(e)})