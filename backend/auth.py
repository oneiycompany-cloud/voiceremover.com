import stripe
import os
from dotenv import load_dotenv
load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def user_is_active(customer_id: str):
    subs = stripe.Subscription.list(customer=customer_id)
    for s in subs:
        if s.status == "active":
            return True
    return False
