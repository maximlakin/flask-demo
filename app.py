import requests
import numpy as np
from bokeh.plotting import figure
from bokeh.embed import components
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
  symbol = request.form['ticker-symbol']
  url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json?api_key=vD5s74xXzwWxuqKYFqYR' % symbol
  req = requests.get(api_url)
  prices = []
  dates = []
  recent = req.json()['data'][0:30]
  recent.reverse()
  for entry in recent:
      prices.append(entry[4])
      dates.append(entry[0])
  plot = figure(
                title='Data from Quandle WIKI set',
                x_axis_label='date',
                x_axis_type='datetime')

  dates = np.array(dates, dtype=np.datetime64)
  prices = np.array(prices)
  plot.line(dates,prices)
  script, div = components(plot)

  return render_template('graph.html', script=script, div=div, symbol=symbol)

if __name__ == '__main__':
  app.run(port=33507)
