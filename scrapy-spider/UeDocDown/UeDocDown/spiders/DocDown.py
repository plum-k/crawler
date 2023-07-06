import scrapy
from pathlib import Path
import json


class DocdownSpider(scrapy.Spider):
    name = "DocDown"
    allowed_domains = ["docs.unrealengine.com"]
    # start_urls = ["http://docs.unrealengine.com/"]

    def start_requests(self):
        content = Path('./x.json').read_text()
        url_list = json.loads(content)
        for url_info in url_list:
            yield scrapy.Request(url=url_info['href'], callback=self.parse, cb_kwargs=url_info)

    def parse(self, response, **kwargs):
        index = {} | kwargs
        main = response.xpath('//div[@id="maincol"]').get()
        index['main'] = main
        yield index
