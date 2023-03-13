import scrapy

class DepthSpider(scrapy.Spider):
    name = "Depth"

    start_urls = ["http://127.0.0.1:48626/"]

    # def start_requests(self):
    #     list = [
    #         {"href": "http://127.0.0.1:48626/nodes/obj/index.html", "text": "OBJ - Object nodes"},
    #         {"href": "http://127.0.0.1:48626/nodes/sop/index.html", "text": "SOP - Geometry nodes"},
    #         {"href": "http://127.0.0.1:48626/nodes/dop/index.html", "text": "DOP - Dynamics nodes"},
    #         {"href": "http://127.0.0.1:48626/nodes/vop/index.html", "text": "VOP - Shader nodes"},
    #         {"href": "http://127.0.0.1:48626/nodes/lop/index.html", "text": "LOP - USD nodes"},
    #         {"href": "http://127.0.0.1:48626/nodes/out/index.html", "text": "ROP - Render nodes"},
    #         {"href": "http://127.0.0.1:48626/nodes/chop/index.html", "text": "CHOP - Channel nodes"},
    #         {"href": "http://127.0.0.1:48626/nodes/cop2/index.html", "text": "COP2 - Compositing nodes"},
    #         {"href": "http://127.0.0.1:48626/nodes/top/index.html", "text": "TOP  - Task nodes"}
    #     ]
    #     node = list[3]
    #     yield scrapy.Request(node['href'], callback=self.parse, cb_kwargs={
    #         'base': node['text']
    #     })

    def parse(self, response):
        li_list = response.xpath('/html/body/main/div[2]/section/div/div[1]/div[2]/section[1]/div/ul/li//a')
        for li in li_list:
            href = response.urljoin(li.xpath('./@href').get())
            text = li.xpath('./text()').get()
            yield scrapy.Request(href, callback=self.node_url_parse, cb_kwargs={
                'base': text
            })

    def node_url_parse(self, response, **kwargs):
        li_list = response.xpath('//ul[@class="subtopics_item_group item_group"]//a[@class="label-text node"]')
        for li in li_list:
            href = response.urljoin(li.xpath('./@href').get())
            text = li.xpath('./text()').get()
            yield scrapy.Request(href, callback=self.node_parse, cb_kwargs={
                                                                               "node_name": text,
                                                                               "href": href
                                                                           } | kwargs)

    def node_parse(self, response, **kwargs):
        index = {'base': kwargs['base'], 'href': kwargs['href'], 'node_name': kwargs['node_name']}
        description_ = response.xpath('/html/body/main/header/div/p[2]/text()').get()
        index['description'] = description_
        description_list = response.xpath('/html/body/main/div/p')
        p_list = []
        for description in description_list:
            p = description.xpath('./text()').get()
            p_list.append(p)
        index['p_list'] = p_list
        parameters_body = response.xpath('//div[@id="parameters-body"]')
        params = []
        if len(parameters_body) == 1:
            div_list = parameters_body[0].xpath('//div[@class="parameter sbs-item "]')
            for div in div_list:
                param = {}
                key = div.xpath('./p[@class="label"]/text()').get()
                if key is not None:
                    param['key'] = key.strip()
                else:
                    param['key'] = ""
                p1_list = div.xpath('./div[@class="content"]//p')
                param['value_list'] = []
                for p1 in p1_list:
                    p = p1.xpath('./text()').get()
                    if p is not None:
                        param['value_list'].append(p.strip())
                params.append(param)
        index['params'] = params
        yield index
