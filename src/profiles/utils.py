import json
import socket
import uuid
from django.contrib.gis.geoip2 import GeoIP2
import requests
import profiles.models 
def get_random_postfix():
   return str(uuid.uuid4())[:10].replace('-','').lower()


# Helper functions

def get_ip_address(request):
   
    host_name = socket.gethostname()    
    IPAddress = socket.gethostbyname(host_name) 
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return IPAddress

def get_geo(ip):
      print(ip)
      ip_address = ip
      if ip=='172.0.0.1':
         ip=''
      # URL to send the request to
      request_url = 'https://geolocation-db.com/jsonp/' 
      # Send request and decode the result
      response = requests.get(request_url)
      result = response.content.decode()
      # Clean the returned string so it just contains the dictionary data for the IP address
      result = result.split("(")[1].strip(")")
      # Convert this data into a dictionary
      result  = json.loads(result)
      print(result)
      country=result['country_name']
      city=result['city']
      lat=result['latitude']
      lon=result['longitude']

      return country, city, lat, lon

def get_center_coordinates(latA, longA, latB=None, longB=None):
    cord = (latA, longA)
    if latB:
        cord = [(latA+latB)/2, (longA+longB)/2]
    return cord

def get_zoom(distance):
    if distance <=100:
        return 8
    elif distance > 100 and distance <= 5000:
        return 4
    else:
        return 2

def invitations_received_no(request):
    if request.user.is_authenticated:
        profile_obj = profiles.Profile.objects.get(user=request.user)
        qs_count = profiles.Relationship.objects.invitations_received(profile_obj).count()
        return {'':qs_count}
    return {}