import json
import os


def format_prediction(stock_name, low, medium, high):
    return f"In the year 2027, I predict {stock_name} will likely be priced at {medium} with a minimum price of {low} and maximum price of {high}."


### Intents Dispatcher ###
def dispatch(prediction_request):
    """
    Called when the user specifies an intent for this bot.
    """

    # Get the name of the current intent
    ticker = prediction_request["currentIntent"]["slots"]["slotOne"]

    # Dispatch to bot's intent handlers
    if ticker == "Prologis":
        return format_prediction('Prologis', 229.24, 250.99, 274.55)
    elif ticker == "American Tower":
        return format_prediction('American Tower', 184.79, 294.09, 384.49)
    elif ticker == "Crown Castle":
        return format_prediction("Crown Castle", 160.74, 237.56, 314.06)
    elif ticker == "Public Storage":
        return format_prediction("Public Storage", 374.31, 685.87, 989.66)
    elif ticker == "Equinix":
        return format_prediction("Equinix", 94.10, 809.05, 1503.25)
    elif ticker == "Simon Property Group":
        return format_prediction("Simon Property Group", 0, 181.39, 422.11)
    elif ticker == "Welltower":
        return format_prediction("Welltower", 30.23, 122.24, 221.01)
    elif ticker == "Digital Realty":
        return format_prediction("Digital Realty", 24.81, 138.53, 253.28)
    elif ticker == "Realty Income":
        return format_prediction("Realty Income", 0, 77.16, 163.68)
    elif ticker == "AvalonBay Communities":
        return format_prediction("AvalonBay Communities", 111.11, 310.72, 498.67)
    else:
        return "I could not find that one"


### Main Handler ###
def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    # print('## ENVIRONMENT VARIABLES')
    # print(os.environ)
    # print('## EVENT')
    # print(event)
    response = dispatch(event)
    return close(event["sessionAttributes"], "Fulfilled", {
        "contentType": "PlainText",
        "content": response
    })


def close(session_attributes, fulfillment_state, message):
    """
    Defines a close slot type response.
    """

    response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": fulfillment_state,
            "message": message,
        },
    }

    return response
