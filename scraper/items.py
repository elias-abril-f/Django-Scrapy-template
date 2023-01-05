# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy_djangoitem import DjangoItem
from main.models import yourmodel


class ScraperItem(DjangoItem):
    django_model = yourmodel