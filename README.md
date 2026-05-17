# HubSpot CRM API Integration Demo

A Python integration with HubSpot's CRM API, built to demonstrate
how SaaS platforms can be connected to automate contact management
and pipeline visibility for sales teams.

## What this does
- Fetches and displays CRM contacts with company data
- Creates new contacts programmatically (simulates onboarding import)
- Retrieves open deals and pipeline stage data

## Why this matters for Solutions Engineers
SEs are often asked to demo API connectivity during evaluations,
help customers with data migration, or validate integration
feasibility. This project simulates that workflow end-to-end.

## Setup
1. Clone the repo
2. Copy `.env.example` to `.env` and add your HubSpot token
3. `pip install -r requirements.txt`
4. `python main.py`

## Tech used
Python 3 · HubSpot CRM API v3 · python-dotenv · requests
