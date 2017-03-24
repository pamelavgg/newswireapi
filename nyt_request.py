import requests
import pandas as pd
import timestring
import datetime

def transform_hours(date):
    start_hour = timestring.Date(date).date
    end_hour = datetime.datetime.now()
    hours = int(divmod((end_hour - start_hour).total_seconds(), 3600)[0])
    return(hours)


def get_data(data, *args):
    for i in range(len(data)):
        dic = dict()
        for argument in args:
            dic[argument] = data[i][argument]
        yield dic


def request(api_key, section, hours):
    url = 'https://api.nytimes.com/svc/news/v3/content/all/' + section + '/' + str(hours) + ' .json'
    response  = requests.get(url, params = {'api-key': api_key}).json()
    results = response['results']
    all_news = list()
    num_results = response['num_results']
    offset = 20

    for news in get_data(results, 'title', 'abstract', 'published_date'):
        all_news.append(news)

    print(str(len(all_news)) + ' news downloaded')

    while num_results > offset:
        response = requests.get(url, params = {'api-key' : api_key, 'offset' : offset}).json()['results']
        for news in get_data(response, 'title', 'abstract', 'published_date'):
            all_news.append(news)

        print(str(len(all_news)) + ' news downloaded')

        offset = offset + 20

    df = pd.DataFrame(all_news)
    df.to_csv("".join(c for c in section if c not in (".", " ")) + '_news.csv')
