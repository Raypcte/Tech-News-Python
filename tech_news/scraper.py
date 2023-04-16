import requests
import time
from parsel import Selector
from .database import create_news


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
    selector = Selector(html_content)
    result = selector.css(".next ::attr(href)").get()
    if result is None:
        return None
    return result


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)

    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css(".entry-title::text").get().strip()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("span.author a::text").get()
    reading_time = int(
        selector.css(".meta-reading-time::text").get().split()[0]
    )
    summary = "".join(
        selector.css(".entry-content > p:nth-of-type(1) ::text").getall()
    ).strip()
    category = selector.css(".category-style span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    base_url = "https://blog.betrybe.com/"
    news_to_insert = []
    news = []

    while len(news_to_insert) < amount:
        current_page = fetch(base_url)
        news_to_insert.extend(scrape_updates(current_page))
        base_url = scrape_next_page_link(current_page)

    # print(len(news_to_insert))
    for url in news_to_insert:
        current_news = fetch(url)
        if len(news) < amount:
            news.append(scrape_news(current_news))

    # print(news)
    create_news(news)
    return news


get_tech_news(2)
