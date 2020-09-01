from google.transit import gtfs_realtime_pb2
import nyct_subway_pb2
import urllib.request

feed = gtfs_realtime_pb2.FeedMessage()
req = urllib.request.Request('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace')
res = urllib.request.urlopen(req)
feed.ParseFromString(res.read())
for entity in feed.entity:
    if entity.HasField('trip_update'):
      # print(entity.trip_update.trip.Extensions[nyct_subway_pb2.nyct_trip_descriptor].train_id)
      for update in entity.trip_update.stop_time_update:
        if update.stop_id.startswith('A32') or update.stop_id.startswith('D20'):
          print(entity.trip_update)