import requests
import json
import re
from config import GEMINI_API_KEY
from flight_status_agent import FlightStatusAgent
from flight_analytics_agent import FlightAnalyticsAgent

class InquiryRouterAgent:
    def __init__(self):
        self.status_agent = FlightStatusAgent()
        self.analytics_agent = FlightAnalyticsAgent()

    def classify_intent_with_llm(self, query):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        headers = {"Content-Type": "application/json"}

        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": f"Classify the following query as 'flight_status' or 'analytics': \"{query}\" Answer:"}
                    ]
                }
            ]
        }

        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            result = response.json()
            return result['candidates'][0]['content']['parts'][0]['text'].strip().lower()
        except Exception as e:
            print("[LLM Error]", e)
            return "analytics"

    def extract_flight_number(self, query):
        match = re.search(r'\b([A-Z]{1,2}\d{2,4})\b', query.upper())
        return match.group(1) if match else None

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