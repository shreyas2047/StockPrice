from flask import Flask, render_template, request
import json, urllib.request


app = Flask(__name__)

#API_KEY
api_key = "zC992yeEkw5VTye5PFJY"

@app.route('/',methods = ['GET', 'POST'])
def getStockPrices():
#POST Method
    if(request.method == 'POST'):
        dates, open_prices, high, low, close, volume, dividend, split = [],[],[],[],[],[],[],[]
# The various stock options available.        
        attr_list = [dates, open_prices, high, low, close, volume, dividend, split]
#API Call
        url_req = urllib.request.urlopen("https://www.quandl.com/api/v3/datasets/EOD/AAPL.json?start_date=2018-01-01&api_key={}".format(api_key))
#Loading the JSON Object        
        json_obj = json.load(url_req)
#Extracting the required data
        data = json_obj.get("dataset").get('data')
#Getting the option from the user
        price = request.form.get('tests')
        if(price == 'high'):
            price = high
        elif(price == 'low'):
            price = low
        elif(price == 'close'):
            price = close
        elif(price == 'volume'):
            price = volume
        elif(price == 'dividend'):
            price = dividend
        elif(price == 'split'):
            price = split
        else:
            price = open_prices
        
        for i in data:
           for j in range(8):
               attr_list[j].append(i[j])
        return render_template('test.html', dates = json.dumps(dates), prices = json.dumps(price))

# GET Method        
    if(request.method == 'GET'):
        return render_template('index.html')

#Starting the Server on port 7777
def main():
    app.run(host="127.0.0.1", port= 7777, debug= True)

if __name__ == '__main__':
    main()