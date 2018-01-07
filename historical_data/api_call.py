import requests
import json

#variables
url = "https://www.alphavantage.co/query"
f = open('history.json', 'r+')

#API Variables
function = "TIME_SERIES_DAILY"
symbol = "SPY"
api_key = "A8YQF0XGD3PZ7JCN"
outputsize = "compact"

#API Params Dictionary
data = { "function": function, 
         "symbol": symbol, 
         "apikey": api_key,
         "outputsize": outputsize,
         }

page = requests.get(url, params = data)

with open('history.json', 'r+') as outfile:
    json.dump(page.json(), outfile, sort_keys=True, indent=4)
    

