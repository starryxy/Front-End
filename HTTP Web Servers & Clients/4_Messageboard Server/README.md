## Messageboard Server

### Summary

**Messageboard1:**

Build a server that accepts a `POST` request and just echoes it back to the browser.

**Messageboard2:**

A `GET` request to the server will return the form, while a `POST` request (submitting the form) will echo back the message.

**Messageboard3:**

Post-Redirect-Get:

1. You go to `http://localhost:8000/` in your browser. Your browser sends a `GET` request to the server, which replies with a `200 OK` and a piece of HTML. You see a form for posting comments, and a list of the existing comments. (But at the beginning, there are no comments posted yet.)

2. You write a comment in the form and submit it. Your browser sends it via `POST` to the server.

3. The server updates the list of comments, adding your comment to the list. Then it replies with a `303 redirect`, setting the `Location: /` header to tell the browser to request the main page via GET.

4. The redirect response causes your browser to go back to the same page you started with, sending a `GET` request, which replies with a `200 OK` and a piece of HTML.


### How to Run

**Messageboard1:**

1. Open up two terminals, in one of them run `python Messageboard1.py`

2. Open `Messageboard.html` and submit to test

3. Keep the Messageboard1 Server running, in another terminal run `python test1.py`

**Messageboard2 & Messageboard3:**

1. Open up two terminals, in one of them run `python Messageboard2.py` OR `python Messageboard3.py`

2. Open `http://localhost:8000/` and submit test

3. Keep the Messageboard2 or Messageboard3 Server running, in another terminal run `python test2.py` OR `python test3.py`
