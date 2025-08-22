from fastapi import APIRouter
from pythonService.services import subscription_service

router = APIRouter()

@router.get("/")
def list_subscriptions():
    # Dummy data for now
    subs = subscription_service.get_mock_subscriptions()
    return {"subscriptions": subs}
