'''Should reply to an inbound text to my Twilio number w/
customized response based on inbound number
'''

from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)

# Try adding your own number to this list!
callers = {
    "+17137489037": "Kojo",
    "+12818448757": "Makiko",
    "+12819281452": "Chanchan!",
}

 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond & greet caller by name."""
 
    from_number = request.values.get('From', None)
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "Monkey, thanks for the message!"

    resp = twilio.twiml.Response()
    resp.message(message)
 
if __name__ == "__main__":
    app.run(debug=True)