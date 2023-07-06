from scrapy import cmdline

# cmdline.execute("scrapy crawl SortUe -O AA.json".split())
# cmdline.execute("scrapy crawl Classes -O quotes.json".split())
# cmdline.execute("scrapy crawl Classes -O quotesEnum.json".split())
cmdline.execute("scrapy crawl Classes -O Fun.json".split())
# cmdline.execute("scrapy crawl Classes".split())
# scrapy shell 'https://docs.unrealengine.com/5.2/en-US/API/Classes/'
# scrapy shell 'https://docs.unrealengine.com/5.2/en-US/API/Runtime/RenderCore/FYUVConvertPS/'
# scrapy shell 'https://docs.unrealengine.com/5.2/en-US/API/Runtime/AIModule/AAIController/'
# scrapy shell 'https://docs.unrealengine.com/5.2/en-US/API/Enums/'