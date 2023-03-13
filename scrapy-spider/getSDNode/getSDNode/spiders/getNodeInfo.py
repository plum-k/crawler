import scrapy


class GetnodeinfoSpider(scrapy.Spider):
    name = "getNodeInfo"
    allowed_domains = ["substance3d.adobe.com"]
    start_urls = ["https://substance3d.adobe.com/documentation/sddoc/node-library-158433312.html#section13"]

    def parse(self, response):
        ul = response.xpath('//ul[@class="childpages-macro conf-macro output-block"]')
        h3_list = response.xpath('//div[@id="page-content-subbody"]//h3/text()')
        for i in range(len(ul)):
            sort = h3_list[i].get()
            a_list = ul[i].xpath('./li/a')
            for j in a_list:
                href = j.xpath("./@href").get()
                text = j.xpath("./text()").get()
                url = response.urljoin(href)
                # print(sort)
                # print(text)
                # print(url)
                yield scrapy.Request(url, callback=self.node_parse, cb_kwargs={
                    "sort": sort,
                    "text": text,
                    "url": url
                })
    def node_parse(self, response, **kwargs):
        index = {} | kwargs
        main = response.xpath('//div[@id="page-content-subbody"]').get()
        index['main'] = main
        yield index
