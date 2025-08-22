from fastapi import FastAPI
from pythonService.api import subscriptions

app = FastAPI(title="ChaKa Subscription Manager")

# Attach routes
app.include_router(subscriptions.router, prefix="/subscriptions", tags=["subscriptions"])

@app.get("/")
def root():
    return {"message": "Welcome to ChaKa Subscription Manager"}
