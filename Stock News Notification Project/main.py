import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_endpoint = "https://www.alphavantage.co/query"
stock_api = "T174BL87GKS9ICHJ"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api
}

stock_response = requests.get(stock_endpoint, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
yesterday_close = float(stock_data["Time Series (Daily)"]["2023-09-11"]["4. close"])
db_yesterday_close = float(stock_data["Time Series (Daily)"]["2023-09-08"]["4. close"])
percentage_difference = round((yesterday_close - db_yesterday_close)*100/db_yesterday_close, 2)

# if percentage_difference > 5 or percentage_difference < -5:
#     print("Get News")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if percentage_difference > 5 or percentage_difference < -5:
    news_endpoint = "https://newsapi.org/v2/everything"
    news_api = "1e3628f58762486f858b03a34155b90c"

    news_parameters ={
        "q": COMPANY_NAME,
        "from": "2023-09-08",
        "to": "2023-09-11",
        "sortBy": "relevancy",
        "apiKey": news_api
    }

    news_response = requests.get(news_endpoint, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data["articles"]
    first_three_articles = articles[:3]

    if percentage_difference > 5:
        up_down = "🔺"
    elif percentage_difference < -5:
        up_down = "🔻"

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.

    for news_article in first_three_articles:
        account_sid = 'AC569ffd0b86cf3dee0c804186d04e8afa'
        auth_token = '250a58f0b0a427157ed325e8201df239'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='+12705409573',
            body=f"""
            TSLA: {up_down}{percentage_difference}%
    Headline: {news_article['title']}. 
    Brief: {news_article['description']}
            """,
            to='+6587424151'
        )

        print(message.status)