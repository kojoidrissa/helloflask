My Twilio/Flask/Heroku app
==========================

For rolling various-sized die via text message. Mostly for D&D.

Send an appropriately formatted string to the the number, it will roll dice for you and return the result(s).

Example
-------
text `2d6`, get back the results of 2 6-sided dice being rolled


STATUS
------
-  The Die class works. The re_match module works. But they need to be adjusted a bit to work with each OTHER and the Twillio app as planned. I'll use `hello_test.py` for that code.
-  hello_reference.py is the working, Twilio example code. hello.py is the code I'm testing. I'm going to incrementally adjust that file until it gets to where I want it to be.
-  2015-11-03: I'm having trouble dealing with NO leading digit before the 'd'. So, I changed the Regex to REQUIRE it. Splitting the message, then running it through str() gives me unicode strings. But the string for '' isn't behaving as I'd expect. So, I'm removing that option for now. I'll have to learn how to deal with it at some point though. I may need to dig into the Twilio API docs to find out what's going on. What data types are being returned, etc.

TESTING
--------
I'm using the Python Testing `unittest tutorial <http://pythontesting.net/framework/unittest/unittest-introduction/>`_ and I'm having trouble getting the "python -m unittest discover simple_example"  to work.

`python test_rematch_unittest.py -v` works fine, as does `python -m unittest -v test_rematch_unittest` but the `python -m unittest discover` option WAS returning "0 tests run". But, now `python -m unittest discover . -v` is working. So, okay.

Turns out, it was a hyphen in the filename. If the testfile is `test_re-match_unittest.py`, the `python -m unittest discover . -v` doesn't work. Removing the hyphen makes it work just fine.

NOTES/REFERENCE
----------------
-  `Twilio Python Quickstart Tutorial <https://www.twilio.com/docs/quickstart/python/sms/replying-to-sms-messages>`_: This is the code base I started from.
-  `Heroku Getting Started with Python docs <https://devcenter.heroku.com/articles/getting-started-with-python-o#running-a-worker>`_ This is what I used, even though Heroku suggests you look at their `new Python docs <https://devcenter.heroku.com/articles/getting-started-with-python#introduction>`_
-  `Heroku Command Line <https://devcenter.heroku.com/categories/command-line>`_ docs