import uuid
import time
import requests
from fake_useragent import UserAgent
from lxml import etree
from requests.adapters import HTTPAdapter

req = requests.Session()
req.mount('https://', HTTPAdapter(max_retries=3))
req.mount('https://', HTTPAdapter(max_retries=3))

req.headers = {'User-Agent': str(UserAgent().random)}

def down(url):
    time.sleep(1)
    print('开始下载:' + url)
    r = req.get(url, timeout=10)
    file_type = "jpg" if r.headers.get("Content-Type") == 'image/jpeg' else "png"
    with open("./images/" + str(uuid.uuid4()) + "." + file_type, 'wb')as f:
        f.write(r.content)
        print('下载成功:' + url)


def getImgUrl(url):
    time.sleep(1)
    r = req.get(url, timeout=10)
    img_root = etree.HTML(r.text)
    img_url = img_root.xpath("/html//div[@class='scrollbox']/img")
    for i in img_url:
        down(i.xpath("@src")[0])


def run(page=1):
    # time.sleep(1)
    url = 'https://wallhaven.cc/toplist?page={}'.format(page)
    print('开始抓取第{}页:'.format(page) + url)
    r = req.get(url, timeout=10)
    html_selector = etree.HTML(r.text)
    a_list = html_selector.xpath("/html//a[@class='preview']")
    for i in a_list:
        getImgUrl(i.xpath('@href')[0])
    print('抓取第{}页结束:'.format(page) + url)


if __name__ == '__main__':
    # todo 7 页之前抓取成功
    for i in range(1, 132):
        run(page=i)
