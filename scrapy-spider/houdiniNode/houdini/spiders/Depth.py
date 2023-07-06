import scrapy

class DepthSpider(scrapy.Spider):
    name = "Depth"
    start_urls = ["http://127.0.0.1:48626/"]

    def start_requests(self):
        list = [
{"href": "http://127.0.0.1:48626/nodes/vex/cvex.html", "text": "CVEX Type"},
{"href": "http://127.0.0.1:48626/nodes/vex/rsl_displace.html", "text": "RSL Displacement Shader"},
{"href": "http://127.0.0.1:48626/nodes/vex/rsl_imager.html", "text": "RSL Imager Shader"},
{"href": "http://127.0.0.1:48626/nodes/vex/rsl_light.html", "text": "RSL Light Shader"},
{"href": "http://127.0.0.1:48626/nodes/vex/rsl_surface.html", "text": "RSL Surface Shader"},
{"href": "http://127.0.0.1:48626/nodes/vex/rsl_volume.html", "text": "RSL Volume Shader"},
{"href": "http://127.0.0.1:48626/nodes/vex/cop2filter.html", "text": "VEX Compositing Filter"},
{"href": "http://127.0.0.1:48626/nodes/vex/cop2gen.html", "text": "VEX Compositing Generator"},
{"href": "http://127.0.0.1:48626/nodes/vex/displace.html", "text": "VEX Displacement Shader"},
{"href": "http://127.0.0.1:48626/nodes/vex/fog.html", "text": "VEX Fog Shader"},
{"href": "http://127.0.0.1:48626/nodes/vex/sop.html", "text": "VEX Geometry Operator"},
{"href": "http://127.0.0.1:48626/nodes/vex/image3d.html", "text": "VEX Image3D Shader"},
{"href": "http://127.0.0.1:48626/nodes/vex/light.html", "text": "VEX Light Shader"},
{"href": "http://127.0.0.1:48626/nodes/vex/chop.html", "text": "VEX Motion and Audio Operator"},
{"href": "http://127.0.0.1:48626/nodes/vex/pop.html", "text": "VEX Particle Operator"},
{"href": "http://127.0.0.1:48626/nodes/vex/photon.html", "text": "VEX Photon Shader"},
{"href": "http://127.0.0.1:48626/nodes/vex/shadow.html", "text": "VEX Shadow Shader"},
{"href": "http://127.0.0.1:48626/nodes/vex/subnet.html", "text": "VEX Subnetwork"},
{"href": "http://127.0.0.1:48626/nodes/vex/surface.html", "text": "VEX Surface Shader"}
]
        node = list[3]
        yield scrapy.Request(node['href'], callback=self.node_url_parse, cb_kwargs={
            'base': node['text']
        })

    # def parse(self, response):
    #     li_list = response.xpath('/html/body/main/div[2]/section/div/div[1]/div[2]/section[1]/div/ul/li//a')
    #     for li in li_list:
    #         href = response.urljoin(li.xpath('./@href').get())
    #         text = li.xpath('./text()').get()
    #         yield scrapy.Request(href, callback=self.node_url_parse, cb_kwargs={
    #             'base': text
    #         })

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
