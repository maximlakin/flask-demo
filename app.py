import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/graph', methods = ['POST'])
def graph():
  url = "https://www.quandl.com/api/v3/datasets/WIKI/"+request.form['ticker-symbol']+".json?api_key=vD5s74xXzwWxuqKYFqYR"
  r = requests.get(url)
  return render_template('graph.html', result = r.json())

if __name__ == '__main__':
  app.run(port=33507)
