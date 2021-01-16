## GET vs. POST

When a browser submits a form via `GET`, it puts all of the form fields into the URI that it sends to the server. These are sent as a query, in the request path — just like search engines do. They're all jammed together into a single line.

When a browser submits a form as a `POST` request, it doesn't encode the form data in the URI path, the way it does with a GET request. Instead, it sends the form data in the request body, underneath the headers. The request also includes Content-Type and Content-Length headers, which we've previously only seen on HTTP responses.


### How to Run

**LoginPage.html & SearchPage.html:**

1. Open `PostForm.html` OR `SearchPage.html` in your browser and don't submit the form yet

2. Open up a terminal and run `python EchoServer.py` on port 8000

3. Go back to browser and submit the form

4. Check HTTP response in terminal

**PostForm.html:**

1. Open `PostForm.html` in your browser and don't submit the form yet

2. Install ncat, which is part of the Nmap network testing toolkit, can be used to investigate how web servers and browsers talk to each other.
`Run brew install nmap`

3. Open up a terminal and run `ncat -l 9999` to listen on port 9999

4. Go back to browser and type some words into the form fields, submit the form

5. Check HTTP response in terminal
