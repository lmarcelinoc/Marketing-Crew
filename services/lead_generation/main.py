import scrapy
import pandas as pd

class LeadSpider(scrapy.Spider):
    name = "leads"
    start_urls = [
        'https://example.com/leads'
    ]

    def parse(self, response):
        for lead in response.css('div.lead'):
            yield {
                'name': lead.css('span.name::text').get(),
                'email': lead.css('span.email::text').get(),
            }

if __name__ == "__main__":
    from scrapy.crawler import CrawlerProcess

    process = CrawlerProcess()
    process.crawl(LeadSpider)
    process.start()
