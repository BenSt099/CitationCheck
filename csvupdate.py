import os
import requests

def update_and_save(email_address):
    api_url = r"https://api.labs.crossref.org/data/retractionwatch?" + email_address
    response = requests.get(api_url)
    with open(os.getcwd() + "/CitationCheck_data_0Ax09a.csv", 'wb') as f:
        f.write(response.content)