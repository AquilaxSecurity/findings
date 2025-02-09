from flask import Flask, render_template, request, escape
from flask_caching import Cache
from ignore.design import design
import datetime

app = design.Design(Flask(__name__), __file__, 'Cache Poisoning')

config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 10,  # Cache duration in seconds
}
app.config.from_mapping(config)
cache = Cache(app)

def cache_key():
    """ Custom cache key function to prevent poisoning """
    return request.remote_addr 

@app.route("/")
@cache.cached(timeout=10, key_prefix=cache_key)
def index():
    timestamp = str(datetime.datetime.now())
    
    referer = request.headers.get("Referer", "Unknown")
    referer = escape(referer) 

    HTMLContent = f'''
    <div id="cache_info">
      <p> The page was cached at: [{timestamp}] </p>
      <p> The user was redirected from: [{referer}] </p>
    </div>
    '''

    return render_template('index.html', result=HTMLContent)
