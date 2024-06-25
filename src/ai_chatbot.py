from transformers import pipeline

def respond_to_query(query):
    """ Respond to a customer query using a pre-trained model """
    chatbot = pipeline('conversational', model='microsoft/DialoGPT-medium')
    response = chatbot(query)
    return response

if __name__ == "__main__":
    query = "What is the status of my recent order?"
    print(respond_to_query(query))