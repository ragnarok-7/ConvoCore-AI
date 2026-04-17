import json
from datetime import datetime

def escalate_query(query):

    record = {

        "query": query,
        "time": str(datetime.now()),
        "status": "Pending"
    }

    with open("database/escalations.json","r") as f:

        data = json.load(f)

    data.append(record)

    with open("database/escalations.json","w") as f:

        json.dump(data,f,indent=4)

    return True