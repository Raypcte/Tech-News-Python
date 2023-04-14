from tech_news.database import search_news
import noticia

# Requisito 7


def search_by_title(title):
    """Seu código deve vir aqui"""
    regex = noticia.compile(title, noticia.I)
    query = {"title": regex}
    res = []
    for news in search_news(query):
        res.append((news["title"], news["url"]))
    return res


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
