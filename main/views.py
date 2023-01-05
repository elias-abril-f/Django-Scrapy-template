from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Scrapy imports
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from scrapy.settings import Settings
import json, scrapy
from multiprocessing import Process, Queue

# Import your spiders here
from scraper.spiders.spider1 import spider1
from scraper.spiders.spider2 import spider2


# Use this function to run the spiders and avoid the "unable to restart reactor" error. 
# Only the spider is needed, the rest of attributes are optional
def run_spider(spider, attribute1, attribute2, ...):
    def f(q):
        try:
            settings = get_project_settings()
            runner = CrawlerRunner(settings)
            # Add any attributes here like this:
            # deferred = runner.crawl(spider, attribute1=attribute1(value), attribute2=value)
            deferred = runner.crawl(spider)
            deferred.addBoth(lambda _: reactor.stop())
            reactor.run()
            q.put(None)
        except Exception as e:
            q.put(e)
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    result = q.get()
    p.join()
    if result is not None:
        raise result

def scrape(request):
    if request.method == "POST":
        
        ########## Parameters for the search form ##########
        form = request.POST
        attribute1= form["attribute1"]
        attribute2 = form["atttribute2"]
        #####################################################
        
        configure_logging()
        # Add spiders here
        spiders = [Spider2, Spider2]
        for spider in spiders:
            run_spider(spider,attribute1, attribute2)
        
        return HttpResponseRedirect(reverse("index"))

def index(request):
    if request.method == "GET":
        try:
            # Load the data we just scraped 
            with open('./main/static/main/data1.json', 'r') as f:
                data = json.load(f)
                with open('./main/static/main/data2.json', 'r') as f:
                    data += json.load(f)
                    return render(request, "main/index.html",{"listings": data})
        except:
            return render(request, "main/index.html")