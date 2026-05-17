from hubspot_client import HubSpotClient
from config import HUBSPOT_TOKEN

def main():
    client = HubSpotClient(HUBSPOT_TOKEN)

    print("\n--- Fetching existing contacts ---")
    contacts = client.get_contacts(limit=5)
    for c in contacts:
        p = c["properties"]
        print(f"  {p.get('firstname')} {p.get('lastname')} | {p.get('email')} | {p.get('company')}")

    print("\n--- Creating a new contact ---")
    new_contact = client.create_contact(
        firstname="Alex",
        lastname="Demo",
        email="alex.demo@acmecorp.com",
        company="Acme Corp"
    )
    print(f"  Created: {new_contact['id']} — alex.demo@acmecorp.com")

    print("\n--- Fetching open deals ---")
    deals = client.get_deals(limit=5)
    for d in deals:
        p = d["properties"]
        print(f"  {p.get('dealname')} | Stage: {p.get('dealstage')} | ${p.get('amount')}")

    print("\nDemo complete.")

if __name__ == "__main__":
    main()
5
Handle config and secrets safely
