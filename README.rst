My Twilio/Flask/Heroku app
==========================

For rolling various-sized die via text message. Mostly for D&D.

Send an appropriately formatted string to the the number, it will roll dice for you and return the result(s).

Example
-------
text `2d6`, get back the results of 2 6-sided dice being rolled


STATUS
------
The Die class works. The re_match module works. But they need to be adjusted a bit to work with each OTHER and the Twillio app as planned. I'll use `hello_test.py` for that code.