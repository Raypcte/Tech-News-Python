from tech_news.database import search_news
import re
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


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
