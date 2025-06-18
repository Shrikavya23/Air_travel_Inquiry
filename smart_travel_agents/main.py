#This class handles all routing of user queries — it decides whether a query should go to the Flight Status Agent or the Flight Analytics Agent.

from inquiry_router_agent import InquiryRouterAgent

if __name__ == "__main__":
    router = InquiryRouterAgent()
    while True:
        query = input("Ask your travel query (or type 'exit'): ")   #Takes user input
        if query.lower() == "exit":
            break
        #inquiry_router handles query and it uses LLM to classify whether it's a flight status or flight analytics
        response = router.handle_query(query)
        print(response)