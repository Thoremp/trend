#coding=utf-8

from lxml import etree
import urllib
import urllib2
import trendUtil
import re

# 解析单页url 返回一页的23条结果
def getSingleHtml(url):
    '解析单页url'
    req = urllib.urlopen(url)
    html = req.read()
    selector = etree.HTML(html)

    # 每页招聘数量
    count = selector.xpath('//*[@id="resultsWrapper"]/div')
    count = len(count)

    # 存储一页的数据
    results = []

    for i in range(1,count):

        result = []
        try:
            url = '//*[@id="resultsWrapper"]/div[' + str(i) + ']/article/div'
            # 招聘详细信息主页
            href = selector.xpath(url + '/div[1]/div[1]/h2/a/@href')
            result.append(href[0])

            # 标题
            title = selector.xpath(url + '/div[1]/div[1]/h2/a/@title')
            result.append(title[0])

            # 该公司所有招聘职位
            company_url = selector.xpath(url + '/div[1]/div[2]/a/@href')
            result.append(company_url[0])

            # 公司名称
            company_name = selector.xpath(url + '/div[1]/div[2]/a/@title')
            result.append(company_name[0])

            # 公司地址
            address = selector.xpath(url + '/div[1]/div[3]/div/p/a/@title')
            result.append(address[0])

            # 发布日期
            date = selector.xpath(url + '/div[3]/p/time/@datetime')
            result.append(date[0][0:10])
            results.append(result)
        except:
            continue
            print u'解析url失败'
        else:
            print u'解析url成功'

    return results

# 获取所有页码的url 入参:url urls(数组)
def getPageUrls(url, pageurls):
    print "当页:" + url
    pageurls.append(url)
    try:
        req = urllib2.urlopen(url)
        html = req.read()
    except:
        return pageurls
    else:

        selector = etree.HTML(html)
        try:
            href = selector.xpath('/html/head/link[@rel="next"]/@href')
        except:
            return pageurls
        else:
            if href:
                # 还有下一页
                url = href[0]
                print "下一页:" + url
                getPageUrls(url, pageurls)
    return pageurls

# 获取所有分类 出参:所有分类url
def getAllUrls():
    '获取所有分类'
    url = 'https://www.monster.com/jobs/search/?q='
    params = ['Python','Java','Hardware','IOS','Android','integrated-circuit','PHP','C++',
            'test-engineer','Embedded','Network','Database','C#','Communications']
    urls = []
    for each in params:
        e = url + each
        urls.append(e)
    return urls

if __name__ == '__main__':
    urls = ['https://www.monster.com/jobs/search/?q=Python&page=2',
            'https://www.monster.com/jobs/search/?q=Python&page=3',
            'https://www.monster.com/jobs/search/?q=Python&page=4']
    for url in urls:
        results = getSingleHtml(url)
        for each in results:
            print each
        break