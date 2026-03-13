from dataclasses import dataclass
import dataclasses
import json

@dataclass
class Ride:
    PULocationID: int
    DOLocationID: int
    trip_distance: float
    total_amount: float
    tpep_pickup_datetime: int  # epoch milliseconds 

# The below Ride is for green trips, for which we handlled
# datetime cols as strings as per assignment instructions. 
@dataclass
class GreenRide:
    lpep_pickup_datetime   : str
    lpep_dropoff_datetime  : str
    PULocationID           : int
    DOLocationID           : int
    passenger_count        : float 
    trip_distance          : float
    tip_amount             : float
    total_amount           : float


def ride_from_row(row):
    return Ride(
        PULocationID=int(row['PULocationID']),
        DOLocationID=int(row['DOLocationID']),
        trip_distance=float(row['trip_distance']),
        total_amount=float(row['total_amount']),
        tpep_pickup_datetime=int(row['tpep_pickup_datetime'].timestamp() * 1000),
    )

def green_ride_from_row(row):
    return GreenRide(
        lpep_pickup_datetime=row['lpep_pickup_datetime'],
        lpep_dropoff_datetime=row['lpep_dropoff_datetime'],
        PULocationID=int(row['PULocationID']),
        DOLocationID=int(row['DOLocationID']),
        trip_distance=float(row['trip_distance']),
        total_amount=float(row['total_amount']),
        tip_amount=float(row['tip_amount']),
        passenger_count=float(row['passenger_count'])
    )

def ride_serializer(ride):
    ride_dict = dataclasses.asdict(ride)
    ride_json = json.dumps(ride_dict).encode('utf-8')
    return ride_json

def ride_deserializer(data):
    json_str = data.decode('utf-8')
    ride_dict = json.loads(json_str)
    return Ride(**ride_dict)


