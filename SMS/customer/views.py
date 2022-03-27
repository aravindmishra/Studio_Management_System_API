from django.shortcuts import render
from customer.controller.controller import Controller
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomerDetailsSerializer
from .models import CustomerDetails, CustomerFileMapping
from datetime import datetime
import logging
# Get an instance of a logging
log = logging.getLogger(__name__)


# Create your views here.

class CreateCustomer(APIView):
    def post(self,request):
        try:
            if Controller.CustomerCreate(request = request):
                return Response({"error":False,"status_code":200,"message":"Data Inserted"})
            else:
                raise KeyError
        
        except KeyError:
            log.error("Invalid Request Data")
            return Response({"error":True,"status_code":400,"message":"Invalid Request Data"})

        except Exception as e:
            log.error(e)
            return Response({"error":True,"status_code":500,"message":str(e)})
