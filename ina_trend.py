#coding=utf-8

import urllib
from lxml import etree
import re
import time
import jp_trendUtil

# 解析单页
def getSinglePage(url):
    req = urllib.urlopen(url)
    html = req.read()
    html = jp_trendUtil.html
    selector = etree.HTML(html)
    divs = selector.xpath('//*[@id="200217000593"]/a/ul/li/text()')
    divs = selector.xpath('//div[@itemtype="http://schema.org/JobPosting"]')
    print len(divs)

    div = divs[0]
    title = div.xpath('//a/ul/li/text()')

    company = div.xpath('//a/span[@class="org"]/text()')

    address = div.xpath('//a/span[@class="loc"]/span/text()')

    time = div.xpath('//div[@class="other_details"]/div[@class="rec_details"]/span[@class="date"]/text()')

    results = []
    i = 0
    for i in range(1, len(title)):
        res = []
        res.append(title[i])
        res.append(company[i])
        res.append(address[i])
        res.append(time[i])
        results.append(res)

    return results

# 获取所有页
def getAllPage(url):
    print url
    req = urllib.urlopen(url)
    html = req.read()
    # html = jp_trendUtil.html
    selector = etree.HTML(html)
    nextPage = selector.xpath('/html/body/div[@class="mainSec"]/div/div[@class="container fl"]/div[@class="srp_container fl  "]/div[@class="pagination"]/a/@href')
    if nextPage:
        getAllPage(nextPage[0])

# 获取所有分类 返回数组 urls
def getAllField():
    url = 'https://www.naukri.com/'
    params = ['Python', 'Java', 'Hardware', 'IOS', 'Android', 'integrated-circuit', 'PHP', 'C++',
              'test-engineer', 'Embedded', 'Network', 'Database', 'Communications', 'Linux']
    urls = []
    for each in params:
        e = url + each + '-jobs'
        urls.append(e)
    return urls

if __name__ == '__main__':
    print 1
    urls = getAllField()
    for each in urls:
        print each