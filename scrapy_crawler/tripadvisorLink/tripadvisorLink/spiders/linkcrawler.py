import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from tripadvisorLink.items import TripadvisorlinkItem


class scrapinglink(Spider):
    name = "tripadvisor_link"
    allowed_domains = ["tripadvisor.ie"]
    start_urls = [
            'https://www.tripadvisor.ie/Restaurants-g294229-Jakarta_Java.html',
            'https://www.tripadvisor.ie/Restaurants-g297704-Bandung_West_Java_Java.html',
            'https://www.tripadvisor.ie/Restaurants-g297715-Surabaya_East_Java_Java.html',
            'https://www.tripadvisor.ie/Restaurants-g294230-Yogyakarta_Java.html',
            'https://www.tripadvisor.ie/Restaurants-g297694-Denpasar_Bali.html',
            'https://www.tripadvisor.ie/Restaurants-g297697-Kuta_Kuta_District_Bali.html',
            'https://www.tripadvisor.ie/Restaurants-g297701-Ubud_Bali.html',
            'https://www.tripadvisor.ie/Restaurants-g297712-Semarang_Central_Java_Java.html',
            'https://www.tripadvisor.ie/Restaurants-g469404-Seminyak_Kuta_District_Bali.html',
            'https://www.tripadvisor.ie/Restaurants-g297710-Malang_East_Java_Java.html',
            'https://www.tripadvisor.ie/Restaurants-g297725-Medan_North_Sumatra_Sumatra.html',
            'https://www.tripadvisor.ie/Restaurants-g297717-Batam_Riau_Archipelago_Riau_Islands_Province.html',
            'https://www.tripadvisor.ie/Restaurants-g297706-Bogor_West_Java_Java.html'
            'https://www.tripadvisor.ie/Restaurants-g297713-Solo_Central_Java_Java.html',
            'https://www.tripadvisor.ie/Restaurants-g311298-Canggu_North_Kuta_Bali.html',
            'https://www.tripadvisor.ie/Restaurants-g297696-Jimbaran_South_Kuta_Bali.html',
            'https://www.tripadvisor.ie/Restaurants-g608487-Legian_Kuta_District_Bali.html',
            'https://www.tripadvisor.ie/Restaurants-g608501-Palembang_South_Sumatra_Sumatra.html'
        ]

    def parse(self, response):
        # process each restaurant link
        urls = response.xpath("//div[contains(@class, 'title')]/a[contains(@class, 'property_title')]//@href").extract()
        for url in urls:
            absolute_url = response.urljoin(url)
            request = scrapy.Request(
                absolute_url, callback=self.parse_restaurant)
            yield request

        # process next page
        next_page_url = response.xpath("//div[contains(@class, 'js_pageLinks')]/a[contains(@class, 'next')]//@href").extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        request = scrapy.Request(absolute_next_page_url)
        yield request

    def parse_restaurant(self, response):
        restaurant = {
            'url': response.url }
        yield restaurant
