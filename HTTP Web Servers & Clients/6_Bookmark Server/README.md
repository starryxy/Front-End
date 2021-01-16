## Bookmark Server

### Summary

A bookmark server or URL-shortening service, similar to <code>TinyURL.com</code>, but with no persistent storage.

This server will accept a URL and a short name, check that the URL actually works (returns an HTTP 200), then store it in a Python dictionary.

- On a GET request to the / path, it displays an HTML form with two fields. One field for the **long URI** you want to shorten, and the other for the **short name**. Submitting this form sends a POST to the server.

- On a POST request, the server looks for the two form fields in the request body. If it has those, it first checks the URI with **requests.get** to make sure that it actually exists (returns a 200).
  - If the URI exists, the server stores a dictionary entry mapping the short name to the long URI, and returns an HTML page with a link to the short version.

  - If the URI doesn't actually exist, the server returns a 404 error page saying so.

  - If either of the two form fields is missing, the server returns a 400 error page saying so.

- On a GET request to an existing short URI, it looks up the corresponding long URI and serves a redirect to it.

### How to Run

1. Open up two terminals, in one of them run `python BookmarkServer.py`

2. Open `http://localhost:8000/` and submit to test

3. Keep the Bookmark Server running, in another terminal run `python test.py`
