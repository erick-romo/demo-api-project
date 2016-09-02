from modules.BreezeClient import Client
import googlemaps
import pprint

gmaps = googlemaps.Client(key='AIzaSyBuBYoY9OiVXnJnQf3D1jFG_iBOjqJkzw8')

geocode_result = gmaps.geocode(address)
latitude = geocode_result[0]["geometry"]["location"]["lat"]
longitude = geocode_result[0]["geometry"]["location"]["lng"]


lat_lon = (latitude, longitude)

client = Client(key = 'dfb5f1f0dcd148ed85b827f2bd133fad', location = lat_lon)

current_conditions = client.current()


air_quality = "\nAir Quality: " + current_conditions["breezometer_description"] + "\nMain Pollutant: " + current_conditions["dominant_pollutant_description"]+ "\nPollutant Causes: " + current_conditions["dominant_pollutant_text"]["causes"]+ "\nHealth Damage from Pollutant: " + current_conditions["dominant_pollutant_text"]["effects"]+ "\nPrecausions for Parents: " + current_conditions["random_recommendations"]["children"]+ "\nHealth Precausions: " + current_conditions["random_recommendations"]["health"]+ "\nIndoor Air Quality: " + current_conditions["random_recommendations"]["inside"]+ "\nOutside Air Quality: " + current_conditions["random_recommendations"]["outside"]+ "\nRecommendations While Sporting: " + current_conditions["random_recommendations"]["sport"]

	
print air_quality

