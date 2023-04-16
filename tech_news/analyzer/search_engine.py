from tech_news.database import search_news
import re
from datetime import datetime
# Requisito 7


def search_by_title(title):
    query_regex = re.compile(title, re.IGNORECASE)
    query = {'title': query_regex}
    news_by_title = []

    for news in search_news(query):
        news_by_title.append((news['title'], news['url']))

    return news_by_title
# Requisito 8


def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        br_date = datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y')
        return [
            (news["title"], news["url"])
            for news in search_news({"timestamp": {"$eq": br_date}})
        ]
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
