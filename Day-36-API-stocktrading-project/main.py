import requests
from secret import secret

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def stock_changed_much():
    # STEP 1: Use https://www.alphavantage.co
    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    stock_api_key = secret.stock_API_KEY
    stock_url = "https://www.alphavantage.co/query"
    stock_params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "apikey": stock_api_key
    }

    res_stock = requests.get(stock_url, stock_params)
    res_stock.raise_for_status()
    stock_data = res_stock.json()
    # print(stock_data)

    (yesterday, day_before) = list(
        stock_data["Time Series (Daily)"].values())[:2]
    print(float(yesterday['5. adjusted close']))
    print(float(day_before['5. adjusted close']))

    difference = float(yesterday['5. adjusted close']) / \
        float(day_before['5. adjusted close'])
    print(difference)

    # += 2 percent difference, get the news
    if difference >= 1.02 or difference <= 0.98:
        return (True, difference)
    else:
        return (False, difference)


def get_news():
    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 2 news pieces for the COMPANY_NAME.
    print('getting news...')
    news_api_key = secret.news_API_KEY
    news_url = "https://newsapi.org/v2/everything"
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": news_api_key,
    }

    resp = requests.get(news_url, news_params)
    resp.raise_for_status()
    news_list = resp.json()
    articles = news_list["articles"][:2]
    return articles


def format_articles(article):
    return f"{STOCK} \n Headline: {article['title']} \n Brief: {article['description']}\n"


def send_sms(text_list):
    # i do not have a twilio account :D
    pass


if stock_changed_much()[0]:
    articles = get_news()

    formatted_articles = [format_articles(art) for art in articles]

    print(formatted_articles[0])

    send_sms(formatted_articles)


# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
