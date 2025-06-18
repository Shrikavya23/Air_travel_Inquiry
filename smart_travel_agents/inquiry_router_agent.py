import requests
import json
import re
from config import GEMINI_API_KEY
from flight_status_agent import FlightStatusAgent
from flight_analytics_agent import FlightAnalyticsAgent

# This class is responsible for classifying the queries
class InquiryRouterAgent:
    def __init__(self):
        self.status_agent = FlightStatusAgent()
        self.analytics_agent = FlightAnalyticsAgent()

    # set up Gemini Flash API endpoint to make API call and query call this function to classify queries
    def classify_intent_with_llm(self, query):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        headers = {"Content-Type": "application/json"}
        
        # Constructing body of requests sent to LLM
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": f"Classify the following query as 'flight_status' or 'analytics': \"{query}\" Answer:"}
                    ]
                }
            ]
        }
        # Sends request and parses json response and final result classifies the query
        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            result = response.json()
            return result['candidates'][0]['content']['parts'][0]['text'].strip().lower()
        except Exception as e:
            print("[LLM Error]", e)
            return "analytics"

    #If the query is about "status" this checks flight number with this format
    def extract_flight_number(self, query):
        match = re.search(r'\b([A-Z]{1,2}\d{2,4})\b', query.upper())
        return match.group(1) if match else None
    
    #Classify the queries
    def handle_query(self, query):
        intent = self.classify_intent_with_llm(query)
        if "status" in intent:
            flight_number = self.extract_flight_number(query)
            if flight_number:
                return self.status_agent.get_flight_status(flight_number)
            return "No valid flight number found."
        elif "analytics" in intent:
            return self.analytics_agent.analyze_query(query)
        return "Sorry, I couldn't understand your query."