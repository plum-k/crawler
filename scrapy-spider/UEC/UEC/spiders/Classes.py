import scrapy

class ClassesSpider(scrapy.Spider):
    name = "Classes"
    allowed_domains = ["docs.unrealengine.com"]
    start_urls = ["https://docs.unrealengine.com/5.2/en-US/API/Functions/"]

    def parse(self, response):
        node_list = []
         # class
        # list = response.xpath('/html/body/div/div[4]/div[1]/div[2]/div[3]/div[@class="memberindexitem"]')
         # enum
        list = response.xpath('//div[@class="memberindexitem"]')
        for a in list:
            node = {}
            node['url'] = response.urljoin(a.xpath('./p/a/@href').get())
            node['title'] = a.xpath('./p/a/span/text()').get()
            node_list.append(node)
        # response.xpath('/html/body/div/div[4]/div[1]/div[2]/div[3]/div[@class="memberindexitem"]')
        # response.xpath('/html/body/div/div[4]/div[1]/div[2]/div[3]/div[@class="memberindexitem"]/p/a/@href').get()
        # response.xpath('/html/body/div/div[4]/div[1]/div[2]/div[3]/div[@class="memberindexitem"]/p/a/span/text()')
        # response.xpath('/html/body/div/div[4]/div[1]/div[2]/div[3]/div[@class="memberindexitem"]/p/a/span/text()').get()
        # url = response.urljoin(a.xpath('./@href').get())
        return node_list
