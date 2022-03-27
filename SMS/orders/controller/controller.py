from datetime import datetime
from orders.models import OrdersDetails
from customer.controller.controller import Controller as customerController

import logging
from customer.models import CustomerDetails

from orders.serializers import CustomerOrderSerailizer, OrdersDetailsSerializer

# Get an instance of a logging
log = logging.getLogger(__name__)

class Controller:
    def createOrder(self,request):
        try:
            customer_id = 0
            # Check input is valid or not.
            validSerializer = CustomerOrderSerailizer(data = request.data)
            if validSerializer.is_valid():
                # Check Customer already exist or not.
                if not customerController().checkCustomerExist(mobile_no = int(validSerializer.data["mobile_no"])):
                    # Create New Customer.
                    if customerController().CustomerCreate(request = request):
                        # Get Last inserted id.
                        customer_id = (CustomerDetails.objects.last()).customer_id
                        print("CREAT",customer_id)
                else:
                    # Filter customer id.
                    customer_id = (CustomerDetails.objects.values('customer_id').filter(mobile_no = int(validSerializer.data["mobile_no"])))[0]["customer_id"]
                    print("EXIST",customer_id)
                    
                if customer_id:
                    # Create a new order.
                    OrdersDetails.objects.create(customer_id = int(customer_id), type = request.data["type"], description = request.data["description"], created_by = 1, created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    log.info("OrdersDetails : Data Inserted")
                    return True
            
            else:
                log.error("CustomerOrderSerailizer :"+str(validSerializer.errors))
                return False
                        
        except Exception as e:
            log.error(e)
            return False