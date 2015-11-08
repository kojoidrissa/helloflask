#Should reply to an inbound text to my Twilio number w/
#customized response based on inbound number

from flask import Flask, request, redirect
import twilio.twiml
from re_match import input_valid
from dice import Die
 
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Take a string describing a die roll, return the roll results"""
 
    # from_number = request.values.get('From', None)
    sent_message = request.values.get('Body')
    if input_valid(sent_message) != None:
        param = sent_message.split('d')
        rolls = int(param[0])
        sides = int(param[-1])

        newdie = Die(sides)
        results = []
        for roll in range(rolls):
            results.append(newdie.roll())
        roll_total = sum(results)

        message = sent_message + "\n" + str(results) + "\n" + str(roll_total)
    else:
        message = sent_message + ''' is not a valid message. Use the
        following format: xdy, where x and y are both numbers between 1 and 99.

        Valid Examples:
        1d8
        2d10
        10d6
        '''

    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp) 
 
if __name__ == "__main__":
    app.run(debug=True)