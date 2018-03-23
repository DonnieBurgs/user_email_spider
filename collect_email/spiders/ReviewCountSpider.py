# coding=utf-8

import scrapy

class CountUserpageSpider(scrapy.Spider):
    name = 'ReviewCountSpider'
    allowed_domains = ['www.amazon.com']

    start_urls = [
        # 'https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=security+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=dusk+to+dawn+led+outdoor+lighting',
        # 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=flood+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=led+motion+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=led+security+motion+sensor+outdoor+lights',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=motion+sensor+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=motion+outdoor+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=motion+spotlight',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=security+spotlight',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=outdoor+motion+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=outdoor+led+lights',
        # # # ------------------------------------------------
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=led+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=warm+light+bulbs',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=ceramic+light+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=150w+led+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=high+lumen+led',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=warehouse+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=barn+bulb',
        # # # ------------------------------------------------
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=greenhouse+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=growing+light+greenhouse',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=indoor+farming+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=indoor+garden+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=led+plant+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=plant+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=smart+garden+grow+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=grow+light',
        # # # ------------------------------------------------
        # 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=smart+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=led+smart+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=app+controlled+lights',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=Color+changing+led+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=dimmable+led+lights',
        # 'https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=led+party+lights',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=led+rgb+smart+home+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=light+bulbs+dimmable',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=music+controlled+bulbs',
        # 'https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=rgb+light+bulbs',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=smart+led+light+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=wifi+light+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=60W+LED+bulbs',
        # 'https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=2700k+led+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=5000k+led+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=A19+led+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=color+temperature+adjustable+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=dimmable+led+bulbs'
    ]

    custom_settings = {
        'RETRY_TIMES': 100,
        # 'DOWNLOAD_DELAY': 2
    }

    keyword_reviewcount_dict = dict()

    def parse(self, response):
        keyword = response.url.split('keywords=')[1].split('&')[0]

        if keyword in self.keyword_reviewcount_dict:
            pass
        else:
            self.keyword_reviewcount_dict[keyword] = 0

        allProductLink = response.xpath('//ul[@id="s-results-list-atf"]/li')
        print('--------------------:', len(allProductLink))
        for item in allProductLink:
            print('\n\n----------------------\n|||||| :', item.xpath("//a[@class = 'a-size-small a-link-normal a-text-normal']/text()").extract_first(), '\n\n----------------------\n')
            count_num_str = str(item.xpath("//a[@class = 'a-size-small a-link-normal a-text-normal']/text()").extract_first()).replace(',', '')
            print('\n\n----------------------\ncount_num_str :', count_num_str, '\n\n----------------------\n')
            if count_num_str == 'None':
                one_item_review_count = 0
            else:
                try:
                    one_item_review_count = int(count_num_str)
                except:
                    one_item_review_count = 0
            print('\n\n----------------------\none_item_review_count :', one_item_review_count, '\n\n----------------------\n')
            self.keyword_reviewcount_dict[keyword] = self.keyword_reviewcount_dict[keyword] + one_item_review_count

        url = response.xpath('//a[@id="pagnNextLink"]/@href').extract_first()

        if url:
            page = "https://www.amazon.com" + url
            yield scrapy.Request(page, callback=self.parse)
        else:
            print(u'---------------------------统计完毕---------------------------')
            print(self.keyword_reviewcount_dict)
            print('--------------------------------------------------------------')