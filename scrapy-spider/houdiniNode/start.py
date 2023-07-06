from scrapy import cmdline

# cmdline.execute("scrapy crawl Houdini -O Houdini_index.json".split())
# cmdline.execute("scrapy crawl GetNodeUrl -O GetNodeUrl.json".split())
cmdline.execute("scrapy crawl Depth".split())
# cmdline.execute("scrapy crawl NodeInfo".split())
# cmdline.execute("scrapy crawl NodeInfo -O NodeInfo.json".split())
# scrapy shell 'http://127.0.0.1:48626/
# scrapy shell 'http://127.0.0.1:48626/nodes/obj/index.html'
# scrapy shell http://127.0.0.1:48626/nodes/vex/index.html



