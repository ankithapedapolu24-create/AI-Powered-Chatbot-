import re


# Predefined customer-support FAQs
FAQS = [
    {
        "keywords": ["hello", "hi", "hey", "good morning", "good evening"],
        "response": "Hello! Welcome to our customer support. How can I help you today?"
    },
    {
        "keywords": ["order", "place order", "buy", "purchase"],
        "response": "You can place an order by selecting a product, adding it to your cart, and clicking the checkout button."
    },
    {
        "keywords": ["track", "tracking", "where", "order status", "delivery status"],
        "response": "You can track your order from the 'My Orders' section. Your tracking information will appear once the order has been shipped."
    },
    {
        "keywords": ["shipping", "delivery", "ship", "deliver"],
        "response": "Standard shipping usually takes 3–5 business days. Delivery times may vary depending on your location."
    },
    {
        "keywords": ["return", "returns", "send back"],
        "response": "We accept returns within 30 days of delivery. The product should be unused and in its original packaging."
    },
    {
        "keywords": ["refund", "money back", "reimburse"],
        "response": "Once your return is approved, refunds are generally processed within 5–7 business days."
    },
    {
        "keywords": ["cancel", "cancellation", "cancel order"],
        "response": "You can request cancellation before your order is shipped. Please contact support as soon as possible."
    },
    {
        "keywords": ["payment", "pay", "payment methods", "card"],
        "response": "We currently support major debit cards, credit cards, and other secure online payment methods."
    },
    {
        "keywords": ["discount", "coupon", "promo", "offer", "promotion"],
        "response": "Discount coupons can be applied during checkout. Please make sure your coupon is valid before placing the order."
    },
    {
        "keywords": ["password", "forgot password", "reset password"],
        "response": "You can reset your password by clicking 'Forgot Password' on the login page and following the instructions."
    },
    {
        "keywords": ["account", "create account", "register", "signup"],
        "response": "To create an account, click the Sign Up button and provide your name, email address, and password."
    },
    {
        "keywords": ["contact", "support", "customer service", "agent"],
        "response": "You can contact our support team through email or live support during business hours."
    },
    {
        "keywords": ["hours", "working hours", "business hours", "open"],
        "response": "Our customer support team is available Monday to Friday from 9:00 AM to 6:00 PM."
    },
    {
        "keywords": ["damaged", "broken", "defective", "wrong product"],
        "response": "We're sorry about that. Please contact support with your order number and a photo of the product so we can assist you."
    },
    {
        "keywords": ["thank", "thanks", "thank you"],
        "response": "You're very welcome! I'm happy to help. Is there anything else you would like to know?"
    },
    {
        "keywords": ["bye", "goodbye", "see you"],
        "response": "Goodbye! Thank you for contacting customer support. Have a great day!"
    }
]


def clean_text(text):
    """
    Basic NLP preprocessing:
    - Convert text to lowercase
    - Remove special characters
    - Remove extra spaces
    """
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()

    return text


def calculate_score(user_text, keywords):
    """
    Calculate how many FAQ keywords
    are present in the user's message.
    """
    score = 0

    for keyword in keywords:
        keyword = keyword.lower()

        if keyword in user_text:
            score += 1

    return score


def get_response(user_message):
    """
    Find the best matching FAQ response.
    """

    cleaned_message = clean_text(user_message)

    if not cleaned_message:
        return "Please enter a message so I can help you."

    best_score = 0
    best_response = None

    for faq in FAQS:
        score = calculate_score(
            cleaned_message,
            faq["keywords"]
        )

        if score > best_score:
            best_score = score
            best_response = faq["response"]

    if best_response:
        return best_response

    return (
        "I'm sorry, I couldn't understand your question. "
        "You can ask me about orders, shipping, returns, refunds, "
        "payments, account issues, discounts, or customer support."
    )
