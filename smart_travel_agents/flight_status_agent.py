import requests
from config import AVIATIONSTACK_API_KEY

#This class is responsible for providing live flight status
class FlightStatusAgent:
    def get_flight_status(self, flight_number):
        url = f"http://api.aviationstack.com/v1/flights?access_key={AVIATIONSTACK_API_KEY}&flight_iata={flight_number}"
        try:
            #sending get request to url and convert response to json format
            response = requests.get(url)
            data = response.json()
            
            #Extracts the "data" field from the json, which contains a list of flights.
            flights = data.get("data", [])
            if not flights:
                return f"No info found for flight {flight_number}."
            
            # Picks first flight from results and extracts relevant details related to flight number
            flight = flights[0]
            airline = flight['airline']['name']
            departure = flight['departure']['airport']
            arrival = flight['arrival']['airport']
            status = flight['flight_status']
            return f"Flight {flight_number} ({airline}) from {departure} to {arrival} is currently {status}."
        except Exception as e:
            return f"Error fetching flight info: {e}"