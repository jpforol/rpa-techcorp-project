from src.data_analysis import top_customers
from src.utils.email_util import send_email

def generate_and_send_report():
    """ Generate top customers report and send it via email """
    report = top_customers()
    report_body = report.to_string(index=False)
    
    send_email(
        to_address='stakeholder@example.com',
        subject='Top Customers Report',
        body=report_body
    )