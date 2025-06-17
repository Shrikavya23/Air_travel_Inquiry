from google.cloud import bigquery
from config import PROJECT_ID, DATASET, TABLE

class FlightAnalyticsAgent:
    def __init__(self):
        self.client = bigquery.Client()

    def analyze_query(self, query):
        origin = "LGA"
        destination = "RDU"
        sql = f"""
                SELECT
                carrier AS airline,
                AVG(arr_delay) AS avg_arrival_delay
                FROM `{PROJECT_ID}.{DATASET}.{TABLE}`
                WHERE origin = '{origin}'
                AND dest = '{destination}'
                AND arr_delay IS NOT NULL
                GROUP BY carrier
                ORDER BY avg_arrival_delay
                LIMIT 3
            """

        try:
            results = self.client.query(sql).result()
            output = f"Top on-time airlines from {origin} to {destination}:\n"
            for i, row in enumerate(results, 1):
                output += f"{i}. {row.airline} (Avg delay: {row.avg_arrival_delay:.2f} min)\n"
            return output
        except Exception as e:
            return f"Error querying BigQuery: {e}"
