import json
import scrapy
from pathlib import Path


class SortueSpider(scrapy.Spider):
    name = "SortUe"
    allowed_domains = ["docs.unrealengine.com"]

    def start_requests(self):
        # nod = {"url": "https://docs.unrealengine.com/5.2/en-US/API/Runtime/AIModule/AAIController", "title": "AAIController"}
        # yield scrapy.Request(url=nod["url"], callback=self.parse, cb_kwargs=nod)
        content = Path('./quotes.json').read_text()
        url_obj = json.loads(content)
        for url in url_obj:
            title = url['title']
            if not (title.startswith("U") or title.startswith("A")) :
                yield scrapy.Request(url=url['url'], callback=self.parse, cb_kwargs=url)

    def parse(self, response, **kwargs):
        text = response.xpath('//td[@class="hierarchy-label-cell"]/p/text()')
        par = ""
        if len(text) == 0:
            par = ""
        else:
            c = []
            a_list = response.xpath('//td[@class="hierarchy-label-cell"]//p/text()')
            for i in a_list:
                c.append(i.get())
            for i in c:
                if i==' ':
                    c.remove(' ')
            index = c.index(kwargs["title"])
            par = c[index-1]
        return {
            "par": par
        } | kwargs
