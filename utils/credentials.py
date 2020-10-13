import json

def load_credentials():
    """loads the credentials file with important stuff in it"""
    with open('credentials.json') as f:
        return json.load(f)
