import urllib.request
from urllib.parse import urlparse
from flask import Flask, request
 
def securelyMakeRequest(url):
  block_schemes = ["file", "gopher", "expect", "php", "dict", "ftp", "glob", "data"]
  block_host = ["internal.localhost"]
  user_supplied_scheme = urlparse(url).scheme
  user_supplied_hostname = urlparse(url).hostname
 
  if user_supplied_scheme in block_schemes:
    return "supplied URL is scheme is forbidden"
 
  if user_supplied_hostname in block_host:
    return "supplied hostname is forbidden"
 
  req = urllib.request.urlopen(url)
  content = req.read()
  return content
 
app = Flask(__name__)
@app.route('/fetchImage')
def fetchImage():
  args = request.args
  url = args.get('url')
  return securelyMakeRequest(url)
 
if __name__ == '__main__':
  app.run()
