import scrapy
from pathlib import Path
import json


class UeDocSpider(scrapy.Spider):
    name = "UeDoc"
    allowed_domains = ["docs.unrealengine.com"]

    # start_urls = ["https://docs.unrealengine.com/5.1/en-US/API/Runtime/Engine/GameFramework/AActor/"]

    # def start_requests(self):
    #     content = Path('./x.json').read_text()
    #     url_obj = json.loads(content)
    #     urls = []

    # def tree_file(path, children):
    #     for i in children:
    #         href = i['href']
    #         name = i['name']
    #         if len(i['child']) != 0:
    #             dir_url = path + i['name'] + "/"
    #             file_url = dir_url + i['name'] + '.md'
    #             urls.append({
    #                 "href": href,
    #                 "name": name,
    #                 "dir_url": dir_url,
    #                 "file_url": file_url
    #             })
    #             tree_file(dir_url, i['child'])
    #         else:
    #             file_url = path + i['name'] + '.md'
    #             urls.append({
    #                 "name": name,
    #                 "href": href,
    #                 "dir_url": path,
    #                 "file_url": file_url
    #             })
    #
    # tree_file("/", url_obj["child"])
    # for url in urls:
    #     yield scrapy.Request(url=url['href'], callback=self.parse, cb_kwargs=url)
    def start_requests(self):
        content = Path('./Fun.json').read_text()
        urls = json.loads(content)

        for url in urls:
            yield scrapy.Request(url=url['url'], callback=self.parse, cb_kwargs=url)

    # # 类
    # def parse(self, response, **kwargs):
    #     print("======================================")
    #     container = response.xpath('//div[@id="pagecontainer"]')[0]
    #
    #     info = response.xpath('//*[@id="pagecontainer"]/div[1]/div[2]')[0]
    #
    #     description = info.xpath('./h2/text()').get()
    #
    #     references = response.xpath('//div[@id="references"]/div/table')[0]
    #
    #     module = references.xpath('./tr[1]/td[2]/p/a/span/text()').get()
    #     header = references.xpath('./tr[2]/td[2]/p/text()').get()
    #     include = references.xpath('./tr[3]/td[2]/p/text()').get()
    #
    #     variables = response.xpath('//div[@id="variables"]/div/table/tr[@class="normal-row"]')
    #     variables_list = []
    #     for variable in variables:
    #         variable_type = variable.xpath('./td[2]/span/p/a/span/text()').get()
    #         if variable_type is None:
    #             variable_type = variable.xpath('./td[2]/span/p/text()').get()
    #
    #         variable_name = variable.xpath('./td[3]//p/text()').get()
    #         variable_description = variable.xpath('./td[4]/p/text()').get()
    #         variables_list.append({
    #             "type": variable_type,
    #             "name": variable_name,
    #             "description": variable_description
    #         })
    #
    #     functions = response.xpath('//div[@id="functions_0"]/div/table/tr[@class="normal-row"]')
    #     functions_list = []
    #     for function in functions:
    #         function_return = function.xpath('./td[2]/span/p/a/span/text()').get()
    #         if function_return is None:
    #             function_return = function.xpath('./td[2]/span/p/text()').get()
    #         function_name = function.xpath('./td[3]/a/nobr/p/text()').get()
    #         function_description = function.xpath('./td[4]/p/text()').get()
    #         is_has = "()" in function_name
    #         functions_list.append({
    #             "return": function_return,
    #             "name": function_name if is_has else function_name + "()",
    #             "description": function_description
    #         })
    #     yield {
    #         "description": description,
    #         "references": {
    #             "module": module,
    #             "header": header,
    #             "include": include,
    #         },
    #         "variables_list": variables_list,
    #         "functions_list": functions_list,
    #     } | kwargs

    #     枚举
    # def parse(self, response, **kwargs):
    #     print("======================================")
    #     container = response.xpath('//div[@id="pagecontainer"]')[0]
    #
    #     info = response.xpath('//*[@id="pagecontainer"]/div[1]/div[2]')[0]
    #
    #     description = info.xpath('./h2/text()').get()
    #
    #     references = response.xpath('//div[@id="references"]/div/table')[0]
    #
    #     module = references.xpath('./tr[1]/td[2]/p/a/span/text()').get()
    #     header = references.xpath('./tr[2]/td[2]/p/text()').get()
    #     include = references.xpath('./tr[3]/td[2]/p/text()').get()
    #
    #     normal_row = response.xpath('//tr[@class="normal-row"]')
    #     normal_row_list = []
    #     for variable in normal_row:
    #         name_cell = variable.xpath('./td[@class="name-cell"]/p/text()').get()
    #         desc_cell = variable.xpath('./td[@class="desc-cell"]/p/text()').get()
    #         normal_row_list.append({
    #             "name": name_cell,
    #             "desc": desc_cell,
    #         })
    #     yield {
    #         "description": description,
    #         "references": {
    #             "module": module,
    #             "header": header,
    #             "include": include,
    #         },
    #         "normal_row_list": normal_row_list,
    #         "variables_list": [],
    #         "functions_list": [],
    #     } | kwargs
    #     函数
    def parse(self, response, **kwargs):
        print("======================================")
        info = response.xpath('//*[@id="pagecontainer"]/div[1]/div[2]')[0]
        description = info.xpath('./h2/text()').get()
        returns = response.xpath('//div[@id="returns"]/p/text()')[0].get()
        normal_row = response.xpath('//tr[@class="normal-row"]')
        normal_row_list = []
        for variable in normal_row:
            name_cell = variable.xpath('./td[@class="name-cell"]/p/text()').get()
            desc_cell = variable.xpath('./td[@class="desc-cell"]/p/text()').get()
            normal_row_list.append({
                "name": name_cell,
                "desc": desc_cell,
            })
        yield {
            "description": description,
            "returns": returns,
            "normal_row_list": normal_row_list,
            "variables_list": [],
            "functions_list": [],
        } | kwargs
