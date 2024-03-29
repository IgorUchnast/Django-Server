from django.db import models
from django.utils import timezone
# Create your models here.

class ShieldBox(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TemperatureSensor(models.Model):
    device = models.ForeignKey(ShieldBox, null=True, on_delete=models.CASCADE)
    name = "tempSensor"
    # time = models.DateTimeField(auto_now_add = True, default=timezone.now)
    time = models.DateTimeField(default=timezone.now)
    temp_value = models.FloatField(max_length = 50)

    def __str__(self):
        return self.name + ' ' + self.device.name + ' - ' + str(self.time.date()) +  ' '  + str(self.time.time()) 
    
class SmokeSensor(models.Model):
    device = models.ForeignKey(ShieldBox, null=True, on_delete=models.CASCADE)
    name = "smokeSensor"
    time = models.DateTimeField(default=timezone.now)
    smoke_value = models.FloatField(max_length = 50)
    def save(self, *args, **kwargs):
        data = kwargs.pop('data', None)
        if data:
            self.smoke_value = data.get('smoke_value', 0.0)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name + ' ' + self.device.name + ' - ' + str(self.time.date()) +  ' '  + str(self.time.time()) 
        # return self.name + ' ' + self.device.name
    