import scrapy
from datetime import timedelta, date

class WODSpider(scrapy.Spider):
    name = "wod"
    custom_settings = {
        'HTTPCACHE_ENABLED': 'True',
        'COOKIES_ENABLED': 'False',
        'AUTOTHROTTLE_ENABLED' : 'True',
        'AUTOTHROTTLE_START_DELAY' : '10.0',
        'AUTOTHROTTLE_DEBUG' : 'True'
    }


    

    def start_requests(self):
        # def daterange(start_date, end_date):
        #     for n in range(int ((end_date - start_date).days)):
        #         yield start_date + timedelta(n)
        allowed_domains = ["crossfitonthehill.com"]
        urls = []
        # start_date = date(2016, 7, 12)
        # end_date = date(2017, 9, )
        # for single_date in daterange(start_date, end_date):
        #     if single_date.weekday() not in [5,6]:
                # urls.append('http://crossfitonthehill.com/category/wod/wod-' + str.lower(single_date.strftime("%m%d%g")))
        for i in range(1,30):
            urls.append('http://crossfitonthehill.com/category/wod/page/' + str(i))
            
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse,headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"})


    def parse(self, response):
        for post in response.xpath('//div[@class="post-content"]/*'):

            yield{
                'all' : post.extract()
                # 'date' : response.xpath('//head/title/text()').extract(),
                # 'workout' : response.xpath('//head/meta[@property="og:description"]/@content').extract()
                }
        #response.xpath('//div[@class="article-content-wrap"]/div/div/text()|//div[@class="article-content-wrap"]/div/text()|//div[@class="article-content-wrap"]/h2/text()|//div[@class="article-content-wrap"]/div/h2/text()|//div[@class="article-content-wrap"]/div/h2/a/text()'):
