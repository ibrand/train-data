import requests

url = 'http://serviceadvisory.nyc/api/stop/A12N/2018-04-30'
api_response = requests.get(url).json()

trips = {}
i = 0
for stop_time in api_response:
    trip_id = api_response[i]['trip']['id']

    stop_time = {
        'duplicate_id': api_response[i]['id'],
        'trip_id': api_response[i]['trip']['id'],
        'route': api_response[i]['trip']['route']['id'],
        'stop_code': api_response[i]['stop']['id'],
        'stop_name': api_response[i]['stop']['name'],
        'timestamp': api_response[i]['timestamp'],
        'progress': api_response[i]['progress'],
    }

    if trip_id not in trips:
        trips[trip_id] = []
    trips[trip_id].append(stop_time)
    trips[trip_id].sort(key=lambda stop_time: stop_time['timestamp'])

    i = i + 1
    
print(trips['135051_A..N'])
