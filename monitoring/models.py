from django.db import models

# Create your models here.
class Store(models.Model):
    store_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    # Add other store-related fields

class StoreStatus(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    timestamp_utc = models.DateTimeField()
    status = models.CharField(max_length=10)  # 'active' or 'inactive'

class BusinessHours(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    day_of_week = models.IntegerField()  # 0=Monday, 6=Sunday
    start_time_local = models.TimeField()
    end_time_local = models.TimeField()

class Timezone(models.Model):
    store = models.OneToOneField(Store, on_delete=models.CASCADE)
    timezone_str = models.CharField(max_length=50)
