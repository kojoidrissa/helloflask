#Should reply to an inbound text to my Twilio number w/ an MMS
from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
 
    resp = twilio.twiml.Response()
    with resp.message("Hello, Mobile Monkey") as m:
        m.media("https://demo.twilio.com/owl.png")
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)


#Should reply to an inbound text to my Twilio number 
from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
 
    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)

#Original hello.py
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World! It's FLASK! And hopefully, WORKING again!"