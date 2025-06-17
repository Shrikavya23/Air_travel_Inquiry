# Air_travel_Inquiry using multi-agents

## Design Choice
*Modular Architecture
The system is split into multiple agents (InquiryRouterAgent, FlightStatusAgent, and FlightAnalyticsAgent) to ensure separation of concerns. Each agent handles a specific type of task—making the code cleaner, reusable, and easier to debug.

*LLM-Based Intent Classification
Instead of relying on hard-coded keyword detection or regex for routing queries, an LLM (Gemini 1.5 Flash API) is used to classify user input as either flight_status or analytics, providing flexibility to handle diverse natural language queries.

*External APIs for Real-Time Data
AviationStack API: Used to fetch real-time flight status information.
Google BigQuery: Used for analyzing large-scale historical flight data, enabling insights like average arrival delays.

*Environment Variable Management
Configuration details (API keys, project IDs, etc.) are kept in a .env file and accessed via config.py to avoid exposing sensitive data in the codebase.

*Interactive CLI Interface
A simple command-line interface is used for user interaction, making it easy to test and demonstrate the functionality.

