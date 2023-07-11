import requests
from dateutil import parser
from users.models import NewsArticle

secret='e1c6f59d2add4b4aae37fbbe8bfbb720'

def get_news_data(text):
    """This function takes a parameter text from user &
    It uses the requests library to make a GET request to the News API with defined parameters.
    it will take the response from NewsAPI in jason format with exception handling .
    save it in db& display the reults on UI.
    """
    parameters = {
    'q': text, 
    'searchIn':'title',
    'language':'en',
    'from': '2023-07-05',
    'sortBy': 'publishedAt',
    'apiKey': secret }
    url = "https://newsapi.org/v2/everything?"
    try:
        response_data = requests.get(url=url, params=parameters)
    except requests.ConnectionError:
        return {"Error": "request connection error with rasa."}
    except requests.exceptions.Timeout:
        return {"Error": "request Timeout error with rasa."}
    except requests.exceptions.TooManyRedirects:
        return {"Error": "request TooManyRedirects error with rasa."}
    except requests.exceptions.RequestException:
        return {"Error": "Oops error with server, check rasa server connections."}
    else:
        if response_data.status_code == 200:
            records = response_data.json()
            for record in records['articles']:
                article = NewsArticle(
                    title=record['title'],
                    source =record['description'],
                    published_at=record['publishedAt']
                   )
                article.save()

            return {"Success": "api request successful", "records": records}
        return {"Error": "Oops invalid request", "Status Code": response_data.status_code}



def get_date(date):
    """This function uses a parser to parse the input date string into a date object """
    yourdate = parser.parse(date)
    return yourdate
    

