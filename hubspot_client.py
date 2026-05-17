import requests

class HubSpotClient:
    BASE_URL = "https://api.hubapi.com"

    def __init__(self, access_token):
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

    def get_contacts(self, limit=10):
        url = f"{self.BASE_URL}/crm/v3/objects/contacts"
        params = {"limit": limit, "properties": "firstname,lastname,email,company"}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()["results"]

    def create_contact(self, firstname, lastname, email, company):
        url = f"{self.BASE_URL}/crm/v3/objects/contacts"
        payload = {
            "properties": {
                "firstname": firstname,
                "lastname": lastname,
                "email": email,
                "company": company
            }
        }
        response = requests.post(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()

    def get_deals(self, limit=5):
        url = f"{self.BASE_URL}/crm/v3/objects/deals"
        params = {"limit": limit, "properties": "dealname,amount,dealstage"}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()["results"]
