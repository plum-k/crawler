from urllib.parse import urljoin

import scrapy


class GetnodeurlSpider(scrapy.Spider):
    name = "GetNodeUrl"
    # allowed_domains = ["127.0.0.1:48626"]
    start_urls = ["http://127.0.0.1:48626/nodes/vex/index.html"]

    def parse(self, response):
        li_list = response.xpath('/html/body/main/div/section/div/div/div/div[2]/ul//a')
        for li in li_list:
            href = urljoin(self.start_urls[0], li.xpath('./@href').get())
            text = li.xpath('./text()').get()
            print(text)
            yield {
                'href': href,
                'text': text
            }
