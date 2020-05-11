import json
import scrapy
from scrapy.http import Request
from scrapy.loader import ItemLoader
from scrapy.item import	Item, Field
from tripadvisor_review.items import TripadvisorReviewItem
from scrapy.selector import Selector

class ReviewsScraper(scrapy.Spider):
    name = "restaurantreviews"
    allowed_domains = ["tripadvisor.ie"]
    f = open("/home/fina/Desktop/tripadvisor_review/tripadvisor_review/tripadvisor_url.json")
    data = json.load(f)
    start_urls = [d['url'] for d in data if 'url' in d]

    def parse(self, response):
        reviews = Selector(response).css('div.non_hotels_like')
        for review in reviews:
            item = TripadvisorReviewItem()
            item['restaurant'] = response.xpath("//h1[contains(@class, 'heading_title')]/text()").extract()
            item['city'] = response.css('div.blEntry span.locality::text').extract()
            item['rating'] = response.css('div.rating span.overallRating::text').extract()
            item['price'] = response.css('div.rating_and_popularity span.header_tags::text').extract()
            item['title_review'] = response.css('div.quote span.noQuotes::text').extract()
            item['review_desc'] = response.css('div.entry p.partial_entry::text').extract()
            yield item
