import pandas as pd
from src.data_ingestion import load_data

def top_customers():
    """ Generate a report of top customers by total amount spent """
    purchase_history = load_data('purchase_history.csv')
    customers = load_data('customers.csv')
    
    # Aggregate total amount spent by each customer
    customer_spend = purchase_history.groupby('cusmoter_id')['total_amount'].sum().reset_index()
    top_customers = customer_spend.nlargest(10, 'total_amount')
    top_customers = top_customers.merge(customers, on='customer_id', how='left')
    
    return top_customers[['customer_id', 'name', 'total_amount']]