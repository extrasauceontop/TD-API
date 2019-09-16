import requests
client_id = "MTSGUGMK4LZAJ1BAWJ0PLPHNKDGJSCXW"

#the daily prices endpoint

# define the endpoint
endPoint = r"https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format('GOOG')

#define our payload
payload = {"apikey":"MTSGUGMK4LZAJ1BAWJ0PLPHNKDGJSCXW",
            "periodType":"day",
            "frequencyType":"minute",
            "frequency":"1",
            "period":"2",
            #"endDate":"1567780200000",
            "startDate":"1554535854000",
            "needExtended":"true"}

# make a request
content = requests.get(url=endPoint, params = payload)

#convert it to a dictionary
data = content.json()

#print(content)
print(data)