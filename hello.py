#Should reply to an inbound text to my Twilio number w/
#customized response based on inbound number

from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)

# Try adding your own number to this list!
# These other number won't work until I upgrade my account
callers = {
    "+17135551212": "Kojo",
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond & greet caller by name."""
 
    from_number = request.values.get('From', None)
    sent_message = request.values.get('Body')
    if from_number in callers:
        message = callers[from_number] + ", thanks for: " + sent_message
    else:
        message = "Caller, thanks for sending me: " + sent_message

    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp) 
 
if __name__ == "__main__":
    app.run(debug=True)