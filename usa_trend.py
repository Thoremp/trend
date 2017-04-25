#coding=utf-8

from lxml import etree
import urllib
import urllib2
import usa_trendUtil
import re
import time
from multiprocessing.dummy import Pool

# 解析单页url 返回一页的23条结果
def getSingleHtml(selector):
    '解析单页url'
    # req = urllib.urlopen(url)
    # html = req.read()
    # selector = etree.HTML(html)

    # 每页招聘数量
    count = selector.xpath('//*[@id="resultsWrapper"]/div')
    count = len(count)

    # 存储一页的数据
    results = []

    for i in range(1, count + 1):

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

    return results

# 获取所有页码的url 入参:url urls(数组)
def getPageUrls(url):

    print u'开始保存:' + url + u' - ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    try:
        req = urllib2.urlopen(url)
        html = req.read()
        selector = etree.HTML(html)
    except:
        print u'解析url出现问题:' + url
    else:


        '''保存当页数据 start'''
        try:
            results = getSingleHtml(selector)
            if results:
                for res in results:
                    print u'正在保存:' + res[0]
                    # 保存之前先检查数据库是否存在这条数据,如果不存在方可保存
                    count = usa_trendUtil.isHaveRecruitUrl(res[0])
                    if(count != 0):
                        usa_trendUtil.saveMessage(res)
                    else:
                        print u'数据库已存在此数据' + res[0]
                        continue
        except:
            print u'保存失败:' + url
        else:
            print u'保存成功:' + url
        '''保存当页数据 end'''

        try:
            href = selector.xpath('/html/head/link[@rel="next"]/@href')
        except:
            print u'解析下一页出现问题:' + url
        else:
            if href:
                # 还有下一页
                url = href[0]
                getPageUrls(url)

# 获取所有分类 出参:所有分类url
def getAllUrls():
    '获取所有分类'
    url = 'https://www.monster.com/jobs/search/?q='
    params = ['Python','Java','Hardware','IOS','Android','integrated-circuit','PHP','C++',
            'test-engineer','Embedded','Network','Database','C#','Communications','Linux']
    urls = []
    for each in params:
        e = url + each
        urls.append(e)
    return urls

if __name__ == '__main__':
    urls = getAllUrls()
    pool = Pool()
    pool.map(getPageUrls, urls)
    pool.close()
    pool.join()