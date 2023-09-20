import stripe
import os
from dotenv import load_dotenv

load_dotenv()
stripe.api_key = os.getenv("STRIPE_API")


def get_stripe(course, user):
    product_create = stripe.Product.create(name=course.title)

    price_create = stripe.Price.create(
        product=product_create.id,
        unit_amount=course.price,
        currency="usd",
    )

    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                'price': price_create,
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='http://127.0.0.1:8000/admin/',
        customer_email=user.email
    )

    # Save these identifiers
    print(f"Success! checkout_session {checkout_session.id}")

    return_data = {
        "payment_id": checkout_session.id,
        "price_id": checkout_session.id,
        "payment_url": checkout_session.url
    }

    return return_data


def get_payment_url(payment_data):
    return payment_data.session.get('payment_url')


def get_status_of_payment(client_secret):
    get_status = stripe.checkout.Session.retrieve(client_secret)
    return get_status
