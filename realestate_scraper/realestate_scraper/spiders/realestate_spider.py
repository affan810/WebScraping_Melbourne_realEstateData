import scrapy
from scrapy_splash import SplashRequest

class RealEstateSpider(scrapy.Spider):
    name = "realestate"
    start_urls = ["https://www.realestate.com.au/agency/tag-real-estate-victoria-WKHCSZ"]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={"wait": 5})

    def parse(self, response):
        # Extract the page title to verify it worked
        title = response.xpath("//title/text()").get()
        print(f"Page Title: {title}")

        # Extract other elements
        property_listings = response.xpath("//div[contains(@class, 'listing-card')]")
        for listing in property_listings:
            yield {
                "title": listing.xpath(".//h2/text()").get(),
                "price": listing.xpath(".//span[contains(@class, 'price')]/text()").get(),
                "address": listing.xpath(".//span[contains(@class, 'address')]/text()").get(),
            }
