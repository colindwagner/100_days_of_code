#pull in stock price of companies we are interested in
#pull in closing price of yesterday and the day before
#compare how muchi t went up or down
#2 pull in the news of the company
# send ourselves an sms of the stock change and news

import requests
from twilio.rest import Client
from datetime import datetime, timedelta
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = NEWS_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_data = stock_response.json()

yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
day_before_yesterday = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')

close_1 = int(float(stock_data["Time Series (Daily)"][yesterday]["4. close"]))
close_2 = int(float(stock_data["Time Series (Daily)"][day_before_yesterday]["4. close"]))

percentage_difference = round((abs(close_1 - close_2) / close_2) * 100.0, 1)

if (close_1 - close_2) < 0:
    arrow = "🔻"
else:
    arrow = "🔺"

if percentage_difference > 5:
    news_params = {
        "q": COMPANY_NAME,
        "from": yesterday,
        "sortBy": "publishedAt",
        "apikey": NEWS_API_KEY
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)

    #list of articles
    news_data = news_response.json()["articles"][0:3]

    sms_content = ""
    for article in news_data:
        sms_content = f'{STOCK} {arrow} {percentage_difference}\nHeadline: {article["title"]}\nBrief: {article["description"]}'
        
        twilio_secret = os.environ.get("TWILIO_SECRET")
        auth_token = os.environ.get("TWILIO_AUTH")
        account_sid = 'ACc9604759e58a2cc4a1570d9fdd82724c' 
        client = Client(account_sid, auth_token) 
        
        message = client.messages.create(  
                                    messaging_service_sid='MGe3af3861ed8ef52782bfef44322f65f3', 
                                    body=sms_content,      
                                    to='+18329935448' 
                                ) 
        print(message.sid)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

