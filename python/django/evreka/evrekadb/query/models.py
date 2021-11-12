from django.db import models

# Creating Foreign Key Vehicle
class Vehicle(models.Model):

    id = models.IntegerField()
    plate = models.CharField(max_length=15, primary_key=True)

    def __str__(self):
        return "Vehicle"

# Creating Navigation Record model
class NavigationRecord(models.Model):

    id = models.IntegerField(primary_key=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, db_constraint=False)
    datetime = models.DateTimeField()
    lattitude = models.FloatField(max_length=10)
    longitude = models.FloatField(max_length=10)

    def __str__(self):
        return "Navigation"
    
def get_last_point():
    last_point = []
    items = NavigationRecord.objects.all()
    fk = Vehicle.objects.all()
    for lat, lon, plate, dt in zip(items.values('lattitude'), items.values('longitude'), items.values('vehicle'), items.values('datetime')):
        last_point.append({'lattitude':lat['lattitude'], 'longitude':lon['longitude'], 'vehicle_plate': plate['vehicle'], 'datetime':dt['datetime'].strftime("%d.%m.%Y, %H:%M:%S")})
    print(last_point)
    return last_point
