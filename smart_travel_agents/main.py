from inquiry_router_agent import InquiryRouterAgent

if __name__ == "__main__":
    router = InquiryRouterAgent()
    while True:
        query = input("Ask your travel query (or type 'exit'): ")
        if query.lower() == "exit":
            break
        response = router.handle_query(query)
        print(response)