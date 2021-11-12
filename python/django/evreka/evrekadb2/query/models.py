from django.db import models
from django.db.models.deletion import CASCADE

# Operation class
class Operation(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

# Bin class
class Bin(models.Model):
    id = models.IntegerField(primary_key=True)
    latitude = models.FloatField(max_length=10)
    longitude = models.FloatField(max_length=10)
    collection_frequency = models.IntegerField()
    last_collection = models.DateTimeField(max_length=15)
    operation = models.OneToOneField(Operation, on_delete=CASCADE, db_constraint=False)

def get_freqs(idb, ido):
    items = Bin.objects.all()
    freqs = []
    for id, lat, lon, cf, lc, op in zip(items.values('id'), items.values('latitude'), items.values('longitude'), items.values('collection_frequency'), items.values('last_collection'), items.values('operation')):
        if id['id'] == idb and op['operation'] == ido:
            freqs.append({'id':id['id'],'latitude':lat['latitude'], 'longitude':lon['longitude'], 'collection_frequency': cf['collection_frequency'], 'last_collection':lc['last_collection'].strftime("%d.%m.%Y, %H:%M:%S"), 'operation':op['operation']})
    print(freqs)
    return freqs