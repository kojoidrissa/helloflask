#Should reply to an inbound text to my Twilio number w/
#customized response based on inbound number

from flask import Flask, request, redirect
import twilio.twiml
from re_match import input_valid
 
app = Flask(__name__)

# Try adding your own number to this list!
# These other number won't work until I upgrade my account


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond & greet caller by name."""
 
    from_number = request.values.get('From', None)
    sent_message = request.values.get('Body')
    if input_valid(sent_message) != None:
        message = "Thanks for: " + sent_message + "Your message is valid."
    else:
        message = "Thanks for sending me: " + sent_message + "but, it's not valid."

    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp) 
 
if __name__ == "__main__":
    app.run(debug=True)