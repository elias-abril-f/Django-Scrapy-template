import scrapy


class Spider2(scrapy.Spider):
    name = 'spider2'
    allowed_domains = ['yourwebsite.']
    
    def __str__ (self):
        return self.name
    
    def __init__(self, *args, **kwargs):
        super(Spider2, self).__init__(*args, **kwargs)
    
    def start_requests(self):
        yield scrapy.Request(f'sites to scrape')

    def parse(self, response):
        
        items = response.css("selector")
        
        for item in items:
                yield{
                    "scrapedData1": item.css(""),
                    "scrapedData2": item.xpath(""),
                }