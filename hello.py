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
        param = sent_message.split('d')
        # if str(param[0]) != '':
        #     rolls = str(param[0])
        # else:
        #     rolls = 1
        message =  "param: " + str(param) + ":*" + str(param[-1]) + "-sided Die: " 
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