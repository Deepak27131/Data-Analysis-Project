# import geocoder

# def get_location():
#     # Get the current location based on IP address
#     g = geocoder.ip('me')
    
#     if g.ok:
#         return {
#             'latitude': g.latlng[0],
#             'longitude': g.latlng[1],
#             'address': g.address
#         }
#     else:
#         return None

# if __name__ == "__main__":
#     location = get_location()
#     if location:
#         print(f"Latitude: {location['latitude']}")
#         print(f"Longitude: {location['longitude']}")
#         print(f"Address: {location['address']}")
#     else:
#         print("Could not retrieve location.")

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium

key = "94a58224d5c84067b3f7fa6550355de6"  # Yahan apni Geocoder API Key daalein
# number = input("Please apna number daalein: ")
# new_number = phonenumbers.parse(number)

number = input("Please apna number daalein: ")  # Example: 9651587120
try:
    # India ke liye "IN" region code specify karein
    new_number = phonenumbers.parse(number, "IN")
    print("Number parsed successfully:", new_number)
except phonenumbers.NumberParseException as e:
    print("Error parsing the number:", e)

location = geocoder.description_for_number(new_number, "en")
print(location)

service_name = carrier.name_for_number(new_number, "en")
print(service_name)

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat, lng)

my_map = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(my_map)

my_map.save("location.html")

print("Location tracking completed")
print("Thank you")

from geopy.geocoders import Nominatim

# Initialize geolocator
geolocator = Nominatim(user_agent="geoapi")

# Coordinates
# Fetch location
location = geolocator.reverse((latitude, longitude))
print("Exact Location:", location.address)
