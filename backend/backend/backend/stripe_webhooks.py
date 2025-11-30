import stripe
import os
from fastapi import APIRouter, Request
from dotenv import load_dotenv
load_dotenv()

router = APIRouter()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")

@router.post("/stripe-webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    signature = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, signature, WEBHOOK_SECRET
        )
    except Exception as e:
        return {"error": str(e)}

    return {"ok": True}
