import json
from datetime import datetime

def save_lead(email=None, phone=None):

    lead = {

        "email": email,
        "phone": phone,
        "time": str(datetime.now())
    }

    with open("database/leads.json","r") as f:

        data = json.load(f)

    data.append(lead)

    with open("database/leads.json","w") as f:

        json.dump(data,f,indent=4)