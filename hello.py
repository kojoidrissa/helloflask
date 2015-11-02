#Should reply to an inbound text to my Twilio number w/
#customized response based on inbound number

from flask import Flask, request, redirect
import twilio.twiml
from re_match import input_valid
from dice import Die

 
app = Flask(__name__)

# Try adding your own number to this list!
# These other number won't work until I upgrade my account

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond with decision about validity of inbound message"""
 
    sent_message = request.values.get('Body')
    if input_valid(sent_message) != None:
        param = sent_message.split('d')
        sides = int(param[-1])
        if param[0] = '':
            rolls = 1
        else:
            rolls = int(param[0])
        
        newdie = Die(sides)
        roll_total = 0
        outcome = []
        
        for roll in range(0, rolls):
            outcome.append(newdie.roll())
        roll_total = sum(outcome)
        message = "You rolled: " + outcome + " for a total of " + roll_total

    else:
        message = "Your input: " + sent_message + " was not valid."

    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp) 
 
if __name__ == "__main__":
    app.run(debug=True)