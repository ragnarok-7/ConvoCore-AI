import json
from datetime import datetime


def classify_lead(products):

    if not products:

        return "Cold",0,"Low",False

    count = len(products)

    if count == 1:

        return "Warm",1,"Medium",False

    if count >= 2:

        return "Hot",count,"High",True


def log_customer_interaction(query, products=None):

    lead_type, score, priority, followup = classify_lead(products)
    
    sales_alert = notify_sales_if_hot(lead_type)

    record = {

        "query": query,

        "products": products,

        "lead_score": score,

        "lead_type": lead_type,

        "priority": priority,

        "followup_required": followup,
        
        "sales_alert": sales_alert,

        "time": str(datetime.now())

    }

    with open("database/crm.json","r") as f:

        data = json.load(f)

    data.append(record)

    with open("database/crm.json","w") as f:

        json.dump(data,f,indent=4)

def notify_sales_if_hot(lead_type):

    if lead_type == "Hot":

        return True

    return False