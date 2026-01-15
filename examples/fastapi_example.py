from fastapi import FastAPI, Request
from ip_geo_alert import process_request
from ip_geo_alert.rules import EndpointRuleEngine

app = FastAPI()

# --------------------------------
# User-defined mail function
# --------------------------------
def send_mail(subject: str, body: str):
    print("\n📧 EMAIL SENT")
    print("Subject:", subject)
    print("Body:", body)


# --------------------------------
# Configure alert endpoints
# --------------------------------
geo_rules = EndpointRuleEngine()

geo_rules.add("/api/v1/login", ["POST"])
geo_rules.add("/api/v1/payment", ["POST"])
geo_rules.add("/api/v1/admin/delete-user")

# --------------------------------
# APIs
# --------------------------------
@app.post("/api/v1/login")
async def login(request: Request):
    process_request(request, send_mail, geo_rules)
    return {"status": "login success"}


@app.post("/api/v1/payment")
async def payment(request: Request):
    process_request(request, send_mail, geo_rules)
    return {"status": "payment success"}


@app.get("/api/v1/profile")
async def profile(request: Request):
    process_request(request, send_mail, geo_rules)
    return {"status": "no alert here"}
