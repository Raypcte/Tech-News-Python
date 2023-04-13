import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    """Seu código deve vir aqui"""
    try:
        result = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        if result.status_code == 200:
            return result.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    all_urls = selector.css("a.cs-overlay-link::attr(href)").getall()
    return all_urls


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    result = selector.css(".next ::attr(href)").get()
    if result is None:
        return None
    return result


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
