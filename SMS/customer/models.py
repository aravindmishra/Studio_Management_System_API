from django.db import models

# Create your models here.

class CustomerDetails(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=720,blank=True,null=True)
    mobile_no = models.BigIntegerField(blank=True,null=True)
    status = models.IntegerField(blank=True,null=True)
    created_by = models.IntegerField(blank=True,null=True)
    created_date = models.DateTimeField(blank=False,null=False)
    modified_by = models.IntegerField(blank=True,null=True)
    modified_date = models.DateTimeField(blank=True,null=True)

    class Meta:
        db_table = "customer_details"


class CustomerFileMapping(models.Model):
    mapping_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField(blank=True,null=True)
    file_id = models.IntegerField(blank=True,null=True)
    type = models.CharField(max_length=120,blank=True,null=True)
    status = models.IntegerField(blank=True,null=True)
    created_by = models.IntegerField(blank=True,null=True)
    created_date = models.DateTimeField(blank=False,null=False)
    modified_by = models.IntegerField(blank=True,null=True)
    modified_date = models.DateTimeField(blank=True,null=True)

    class Meta:
        db_table = "customer_file_mapping"
