import requests
from config import AVIATIONSTACK_API_KEY

class FlightStatusAgent:
    def get_flight_status(self, flight_number):
        url = f"http://api.aviationstack.com/v1/flights?access_key={AVIATIONSTACK_API_KEY}&flight_iata={flight_number}"
        try:
            response = requests.get(url)
            data = response.json()
            flights = data.get("data", [])
            if not flights:
                return f"No info found for flight {flight_number}."

            flight = flights[0]
            airline = flight['airline']['name']
            departure = flight['departure']['airport']
            arrival = flight['arrival']['airport']
            status = flight['flight_status']
            return f"Flight {flight_number} ({airline}) from {departure} to {arrival} is currently {status}."
        except Exception as e:
            return f"Error fetching flight info: {e}"