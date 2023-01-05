import scrapy


class Spider1(scrapy.Spider):
    name = 'spider2'
    allowed_domains = ['yourwebsite.com']
    
    def __str__ (self):
        return self.name
    
    def __init__(self, *args, **kwargs):
        super(Spider1, self).__init__(*args, **kwargs)
    
    def start_requests(self):
        yield scrapy.Request(f'sites to scrape.com/data....')

    def parse(self, response):
        
        items = response.css("selector")
        
        for item in items:
                yield{
                    "scrapedData1": item.css("").attrib[""],
                    "scrapedData2": item.xpath(""),
                }