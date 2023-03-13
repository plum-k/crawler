import scrapy


class VexfunSpider(scrapy.Spider):
    name = "VEXFUN"
    # allowed_domains = ["127.0.0.1:48626"]
    start_urls = ["http://127.0.0.1:48626/vex/functions/index.html"]

    def parse(self, response):
        sections = response.xpath("/html/body/main/div/section/div/div/div/div[2]//section")
        for i in sections:
            h2 = i.xpath("./h2/text()").get().strip()
            urls = i.xpath('.//a[@class="label-text vex"]/@href')
            for j in urls:
                url = "http://127.0.0.1:48626/vex/functions/"+j.get()
                yield scrapy.Request(url, callback=self.parse_info, cb_kwargs={
                    "h2": h2,
                    "url": url,
                })

    def parse_info(self, response, **kwargs):
        main = response.xpath("//main").get()
        h1 = response.xpath("//h1/text()").get()
        index = {} | kwargs
        index['main'] = main
        index['h1'] = h1.strip()
        yield index
