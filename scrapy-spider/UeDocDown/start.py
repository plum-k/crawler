from scrapy import cmdline

# cmdline.execute("scrapy crawl DocDown -O quotes.json".split())
cmdline.execute("scrapy crawl DocDown".split())
# scrapy shell 'https://docs.unrealengine.com/5.2/zh-CN/'
