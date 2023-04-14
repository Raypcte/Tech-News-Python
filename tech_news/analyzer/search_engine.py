from tech_news.database import search_news

# Requisito 7


def search_by_title(title):
    """Seu código deve vir aqui"""
    found_news = list()
    query = {"titleNews": {"$regex": title.lower()}}

    for news in search_news(query):
        found_news.append((news["titleNews"], news["news"]))

    return found_news


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
