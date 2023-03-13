from urllib.parse import urljoin

import scrapy


class HoudiniSpider(scrapy.Spider):
    name = "Houdini"
    start_urls = ["http://127.0.0.1:48626/"]

    def parse(self, response):
        li_list = response.xpath('/html/body/main/div[2]/section/div/div[1]/div[2]/section[1]/div/ul/li//a')
        for li in li_list:
            href = urljoin(self.start_urls[0], li.xpath('./@href').get())
            text = li.xpath('./text()').get()
            yield {
                'href': href,
                'text': text
            }
