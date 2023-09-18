import stripe
import os
from dotenv import load_dotenv


load_dotenv()


def get_stripe(course, user):
    stripe.api_key = os.getenv("STRIPE_API")

    starter_subscription = stripe.Product.create(
        name=course.title,
    )

    starter_subscription_price = stripe.Price.create(
        unit_amount=course.price,
        currency="eur",
        recurring={"interval": "month"},
        product=starter_subscription.id,
    )

    payment_create = stripe.PaymentIntent.create(
        amount=starter_subscription_price.unit_amount,
        currency="usd",
        receipt_email=user.email,
        payment_method_types=['card'],
    )

    payment_retrieve = stripe.PaymentIntent.retrieve(
        payment_create.id,
    )
    payment_link = stripe.PaymentLink.create(line_items=[{"price": starter_subscription_price.id, "quantity": 1}])

    # Save these identifiers
    print(f"Success! payment_create {payment_create.id}")
    print(f"Success! payment_retrieve {payment_retrieve.id}")
    print(f"Success! payment_link {payment_link.url}")

    return payment_retrieve.id


def get_status_of_payment(client_secret):

    get_status = stripe.PaymentIntent.retrieve(
        client_secret,
    )

    return get_status
