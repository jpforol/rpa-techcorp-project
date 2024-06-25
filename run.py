from src.data_ingestion import load_data, clean_data
from src.data_analysis import top_customers
from src.report_generation import generate_and_send_report
from src.ai_chatbot import respond_to_query

def main():
    print("Welcome to the Intelligent Customer Interaction and Data Processing System")

    # Example: Load and clean customer data
    print("Loading and cleaning customer data...")
    customers = load_data('customers.csv')
    customers = clean_data(customers)
    print(customers.head())

    # Example: Generate top customers report
    print("Generating top customers report...")
    top_customers_report = top_customers()
    print(top_customers_report)

    # Example: Send the top customers report via email
    print("Sending top customers report via email...")
    generate_and_send_report()

    # Example: Respond to a customer query
    print("Responding to a customer query...")
    query = "What is the status of my recent order?"
    response = respond_to_query(query)
    print(f"Chatbot response: {response}")

if __name__ == "__main__":
    main()
