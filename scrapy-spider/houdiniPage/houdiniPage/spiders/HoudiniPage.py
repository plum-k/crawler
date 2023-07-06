import scrapy


class HoudinipageSpider(scrapy.Spider):
    name = "HoudiniPage"
    allowed_domains = ["www.sidefx.com"]
    start_urls = ["https://www.sidefx.com/docs/houdini/basics/index.html"]

    def parse(self, response):
        # hitlist = response.xpath('//div[@class="hitlist "]')
        hitlist = response.xpath('//div[@id="subtopics-body"]')
        print(hitlist)
        a_s = hitlist.xpath(".//a")
        print(a_s)
        for a in a_s:
            url = response.urljoin(a.xpath('./@href').get())
            title = a.xpath('./text()').get()
            yield scrapy.Request(url, callback=self.parse_page, cb_kwargs={
                'title': title,
                "url": url,
            })

    def parse_page(self, response, **kwargs):
        content = response.xpath('//div[@id="content"]')[0].get()
        index = {} | kwargs
        index['content'] = content
        yield index
