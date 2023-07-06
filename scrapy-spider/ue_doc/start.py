from scrapy import cmdline

# cmdline.execute("scrapy crawl UeDoc -O quotes.json".split())
cmdline.execute("scrapy crawl UeDoc".split())


# scrapy shell 'https://docs.unrealengine.com/5.1/en-US/API/Runtime/Engine/GameFramework/AActor/'
# scrapy shell 'https://docs.unrealengine.com/5.2/en-US/API/Runtime/Core/IsInGameThread/'

# from scrapy.item import Item, Field
#
# from scrapy.contrib.loader import ItemLoader
#
# from scrapy.contrib.loader.processor import TakeFirst
#
# class MetaItem(Item):
#
#     url = Field()
#
#     added_on = Field()
#
# class MainItem(Item):
#
#     price = Field()
#
#     title = Field()
#
#     meta = Field(serializer=MetaItem)
#
# class MainItemLoader(ItemLoader):
#
#     default_item_class = MainItem
#
#     default_output_processor = TakeFirst()
#
# class MetaItemLoader(ItemLoader):
#
#     default_item_class = MetaItem
#
#     default_output_processor = TakeFirst()
#
#
# from scrapy.spider import Spider
#
# from qwerty.items import MainItemLoader, MetaItemLoader
#
# from scrapy.selector import Selector
#
# class DmozSpider(Spider):
#
#     name = "dmoz"
#
#     allowed_domains = ["example.com"]
#
#     start_urls = ["http://example.com"]
#
#     def parse(self, response):
#         mainloader = MainItemLoader(selector=Selector(response))
#
#         mainloader.add_value('title', 'test')
#
#         mainloader.add_value('price', 'price')
#
#         mainloader.add_value('meta', self.get_meta(response))
#
#     return mainloader.load_item()
#
#     def get_meta(self, response):
#
#         metaloader = MetaItemLoader(selector=Selector(response))
#
#         metaloader.add_value('url', response.url)
#
#         metaloader.add_value('added_on', 'now')
#
#         return metaloader.load_item()