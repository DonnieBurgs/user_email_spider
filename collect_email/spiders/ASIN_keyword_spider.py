# coding= utf-8

import scrapy
from collect_email.items import AsinKeywordItem


class AsinKeywordSpider(scrapy.Spider):
    name = 'AsinKeywordSpider'
    allowed_domains = ['www.amazon.com']
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Referer': 'None'
    }

    start_urls = [
        'https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=security+light',
        'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=grow+light',
        'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=smart+bulb',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=led+smart+bulb',
        'https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=app+controlled+lights',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=Color+changing+led+bulb',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=dimmable+led+lights',
        'https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=led+party+lights',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=led+rgb+smart+home+bulb',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=light+bulbs+dimmable',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=music+controlled+bulbs',
        'https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=rgb+light+bulbs',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=smart+led+light+bulb',
        'https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=wifi+light+bulb',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=60W+LED+bulbs',
        'https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=2700k+led+bulb',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=5000k+led+bulb',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=A19+led+bulb',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=color+temperature+adjustable+bulb',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=dimmable+led+bulbs'
    ]

    custom_settings = {
        'RETRY_TIMES': 100,
        # 'DOWNLOAD_DELAY': 0.5,
        'ITEM_PIPELINES': {
            'collect_email.pipelines.UserEmailPipeline': 1
        }
    }

    index = 0
    ASIN_Keyword_set = set()

    def parse(self, response):
        keyword = response.url.split('keywords=')[1].split('&')[0]

        allProductLink = response.xpath('//ul[@id="s-results-list-atf"]/li')
        for item in allProductLink:
            asin = item.xpath('@data-asin').extract_first()
            if asin + keyword in self.ASIN_Keyword_set:
                pass
            else:
                self.index = self.index + 1
                self.ASIN_Keyword_set.add(asin + keyword)

                asin_keyword_item = AsinKeywordItem()
                asin_keyword_item['index'] = self.index
                asin_keyword_item['asin'] = asin
                asin_keyword_item['keyword'] = keyword

                yield asin_keyword_item

        url = response.xpath('//a[@id="pagnNextLink"]/@href').extract_first()

        if url:
            page = "https://www.amazon.com" + url
            yield scrapy.Request(page, callback=self.parse)
        else:
            print('All Products have been searched !!!')