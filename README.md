# Multi-agents for Air travel inquiry

## Set up Instructions:
1.	Created a virtual environment and activate that
	- Command: python –m venv air_travel_agents <br> air_travel_agents\source\activate

2.	Created a folder smart_travel_agents to add all files

	Initially create requirements.txt: contain libraries to install namely
	- requests: to make http calls to Gemini and Aviationstack APIs
	- google-cloud-biquery : To interact with google BigQuery
	- python-dotenv : To load API keys from .env file
	Finally pip install –r requirements.txt
	Created an .env file that contains API keys namely Gemini API key, Aviationstack API key, info about dataset name, tables 	and project_id. This file is later added to .gitignore so that it is not accessible by others. 

3.	Downloaded google SDK so that I can interact with google cloud services through terminal.
   		 After that run gcloud init: to set up google cloud project
				gcloud auth application-default login: authenticate so local code can use Bigquery and APIs.

4.	Set up Google BigQuery
	- Created a project air_travel_multi_agents and noted the project_id.
	- Enable Google BigQuery API
	- Added dataset with flights_dataset name
	- Created table and then uploaded dataset with .CSV format

5.	Started creating .py files
	main.py:
	- This is the entry point of program. 
	- Takes user input and instantiate the inquiry_router.
	- Inquiry_router will handle the query using LLM and classify the query as flight_status or flight_analytics.
	- Depending on this, flight_status will make an Aviationstack API call and flight_analytics will run BigQuery query.

	inquiry_router_agent.py:
	- When a user type his query it is passed to this agent.
	- Setting up the API endpoint and make call to Gemini API.
	- Asking LLM to classify two types of queries.
	- If the query is about status, it tries to extract a flight number and forwards it to the status agent. 
	- If the query is about analytics, it forwards the full query to the analytics agent.

	flight_status_agent.py
	- If the query is about flight_status the inquiry_router points this agent.
	- This method takes a flight number (like "AI302") as input.
	- Construct the API URL using the base URL of AviationStack, inserting API key.
	- This agent retrieves information like Airline name, Departure airport name, Arrival airport name, Flight status (e.g., 	active, landed, cancelled) for relevant flight number.

	flight_analytics_agent.py
	- If the query is about flight_analytics the inquiry_router points to this agent.
	- This is responsible for handling analytical queries related to flight data.
	- Uses BigQuery client library to run SQL queries on datasets hosted in Google Cloud.
	- Based on sql queries returns the result.

	config.py
	- This config.py file securely loads API keys and project configuration values from a .env file using environment 		variables.


## Design Choice
*Modular Architecture:
The system is split into multiple agents (InquiryRouterAgent, FlightStatusAgent, and FlightAnalyticsAgent) to ensure separation of concerns. Each agent handles a specific type of task—making the code cleaner, reusable, and easier to debug.
 - InquiryRouterAgent routes queries using Gemini LLM.
 - FlightStatusAgent handles live flight status using AviationStack API.
 - FlightAnalyticsAgent uses BigQuery for historical flight analysis.
 

*LLM-Based Intent Classification:
Instead of relying on hard-coded keyword detection or regex for routing queries, an LLM (Gemini 1.5 Flash API) is used to classify user input as either flight_status or analytics, providing flexibility to handle diverse natural language queries.

*External APIs for Real-Time :
- AviationStack API: Used to fetch real-time flight status information.
- Google BigQuery: Used for analyzing large-scale historical flight data, enabling insights like average arrival delays.

*Environment Variable Management:
Configuration details (API keys, project IDs, etc.) are kept in a .env file and accessed via config.py to avoid exposing sensitive data in the codebase.

*Interactive CLI Interface:
A simple command-line interface is used for user interaction, making it easy to test and demonstrate the functionality.

