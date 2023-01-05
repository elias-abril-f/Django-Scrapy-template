# Django-Scrapy-template
## A template for a Django powered webapp with Scrapy integration

This is an almost ready to use template for a Django webapp that can use the Scrapy framework to scrape data from the web. 
Most of the heavy lifting is done, as Scrapy is installed as an app within django and there is a function to take care of the reactor error (if you are not
careful and scrapy is not integrated properly you'll be able to run your spiders once and the reactor will not shut off properly, so next time you try to 
run them you'll get the dreaded "reactor can not be restarted"). 

## How to use
Just download the files and change the placeholders for your spiders names, attributes and simmilar. You can also change the title of your project, just
find all instances of "crawler" and change it. Everything else should work straight away, just add your own project on top of the basic integrated template. 
