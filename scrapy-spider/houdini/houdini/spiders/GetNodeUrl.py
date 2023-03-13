from urllib.parse import urljoin

import scrapy


class GetnodeurlSpider(scrapy.Spider):
    name = "GetNodeUrl"
    allowed_domains = ["127.0.0.1:48626"]
    start_urls = ["http://127.0.0.1:48626/nodes/obj/index.html"]

    def parse(self, response):
        li_list = response.xpath('/html/body/main/div/section[2]/div/div/div/div[2]/ul/li//a')
        for li in li_list:
            href = urljoin(self.start_urls[0], li.xpath('./@href').get())
            text = li.xpath('./text()').get()
            yield {
                'href': href,
                'text': text
            }
