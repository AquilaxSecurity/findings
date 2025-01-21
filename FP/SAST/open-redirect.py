from flask import Flask, request, redirect, abort 
from urllib.parse import urlparse

app = Flask (name_)

ALLOWED_DOMAINS = ["website.com", "test.com"]

@app. route("/redirect", methods= ["GET"'])
def safe_redirect():
   target = request.args. get("url")
   if not target:
      return abort(400, "Missing redirect target")
parsed_url = urlparse (target)

if parsed_url.netloc not in ALLOWED_DOMAINS:
   return abort(400, "Invalid redirect domain")

return redirect (target)
