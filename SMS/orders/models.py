from django.db import models

# Create your models here.
class OrdersDetails(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField(blank=True,null=True,db_index=True)
    type = models.CharField(max_length=220,blank=True,null=True)
    description = models.CharField(max_length=1200,blank=True,null=True)
    status = models.IntegerField(blank=True,null=True)
    created_by = models.IntegerField(blank=True,null=True)
    created_date = models.DateTimeField(blank=False,null=False)
    modified_by = models.IntegerField(blank=True,null=True)
    modified_date = models.DateTimeField(blank=True,null=True)

    class Meta:
        db_table = "orders_details"

    def OrdersDetailsList():
        query = '''SELECT od.order_id, cd.name , od.order_id, cd.name , cd.mobile_no, od.type, od.description ,cd.customer_id, od.created_date FROM orders_details od 
	                LEFT JOIN customer_details cd ON cd.customer_id = od.customer_id 
	                ORDER BY od.order_id DESC '''
        return OrdersDetails.objects.raw(query)



class FileDetails(models.Model):
    file_id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=720,blank=True,null=True)
    file_path = models.CharField(max_length=1220,blank=True,null=True)
    size_in_kb = models.BigIntegerField(blank=True,null=True)
    type = models.CharField(max_length=220,blank=True,null=True)
    status = models.IntegerField(blank=True,null=True)
    created_by = models.IntegerField(blank=True,null=True)
    created_date = models.DateTimeField(blank=False,null=False)
    modified_by = models.IntegerField(blank=True,null=True)
    modified_date = models.DateTimeField(blank=True,null=True)

    class Meta:
        db_table = "file_details"
