from customer.models import CustomerDetails
from customer.serializers import CustomerDetailsSerializer
from datetime import datetime
import logging

# Get an instance of a logging
log = logging.getLogger(__name__)

class Controller:
    def CustomerCreate(self,request):
        try:
            # Create a new Customer.
            serializer = CustomerDetailsSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save(created_by = 1, created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                log.info("Data Inserted")
                return True
            log.error(serializer.errors)
            return False
  
        except Exception as e:
            log.error(e)
            return False

    def checkCustomerExist(self,mobile_no):
        try:
            if mobile_no and isinstance(mobile_no,int):
                # Check mobile_no is exist in customer_details table.
                count = CustomerDetails.objects.filter(mobile_no = int(mobile_no)).count()
                return True if count != 0 else False
  
        except Exception as e:
            log.error(e)
            return False