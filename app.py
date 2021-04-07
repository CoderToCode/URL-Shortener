from flask import Flask, redirect, url_for

app = Flask(__name__)

short = ["google", "fb", "ecampusKG", "github"]
url = ["https://www.google.co.in", "https://www.facebook.com", "https://ecampus.kgisliim.ac.in/ecampus/mst_users/index", "https://github.com/CoderToCode"]

@app.route('/')
def hello_world():
   return 'Welcome to URL Shortener by CoderToCode(SAGAR K)'

@app.route('/<short_url>')
def url_shortener(short_url):
      link = url[short.index(short_url)]
      return redirect(link)

@app.route('/create/<big_url>=<small_url>')
def url_create(big_url, small_url):
      short.append(small_url)
      url.append(big_url)
      return "Your Url - " + big_url + "has been shortened to " + small_url

if __name__ == '__main__':
   app.run(host='0.0.0.0')