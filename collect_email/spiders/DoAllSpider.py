# coding=utf-8

import scrapy
import time
import xlrd
from collect_email.items import UserEmailItem, AsinKeywordItem, AsinOfErrorItem
from collect_email.settings import COOKIE

from sqlalchemy.sql import func
from collect_email.db_manage import sessionmaker, UserEmails, AsinKeyword, AsinOfError, engine
Session = sessionmaker()
Session.configure(bind = engine)
session = Session()


class DoAllSpider(scrapy.Spider):
    name = 'DoAllSpider'
    allowed_domains = ['www.amazon.com']
    cookie = COOKIE
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Referer': 'None'
    }

    start_urls = [
        # # 安防灯//20171110//201711141639//201711170906--201711171807//201711211000--201711220900//201711232026--201711240233//201712051630--201712060740
        # 201712071050--201712081733//201712081807--201712092037//201712110910--201712120034//201712121717--201712131623//
        # 201712140910--201712141808//
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
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=dusk+to+dawn+lights',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=flood+light+outdoor',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=led+motion+security+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=led+motion+sensor+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=led+security+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=led+security+lights',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=led+spotlight',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=motion+sensor+light+outdoor',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=motion+sensor+security+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=outdoor+motion+flood+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=outdoor+motion+lights',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=outdoor+motion+sensor+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=outdoor+security+lights',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=security+light+motion+sensor',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=security+lights+motion+outdoor',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=security+sensor+lights+outdoor',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=sensor+security+light',
        # # 球泡灯//20171110//201711141639//201711160915--201711170900//201711171812--201711201400//201711220915--201711231800//201711232026--201711240233//201712051630--201712060740
        # 201712071050--201712081733//201712081807--201712092037//201712110910--201712120034//201712121717--201712131623//
        # 201712140910----201712141808//
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=led+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=warm+light+bulbs',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=ceramic+light+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=150w+led+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=high+lumen+led',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=warehouse+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=barn+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=hall+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=3+way+light+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=led+bay+light+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=dimmable+led+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=led+bulbs',
        # 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=led+light+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=30w+led+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=250+watt+light+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=6500k+led+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=high+lumen+led+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=150+watt+light+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=150+watt+led+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=200+watt+led+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=200w+led',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=led+bulbs+daylight',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=250w+led+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=led+bulb+250+watt',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=150+w+led+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=200+watt+light+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=3+way+led+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=light+bulb',
        # # 植物生长灯//20171114//201711151821-201711160900//201711171812--201711201400//201711220915--201711231800//201711232026----201711240233//
        # 201712060910--201712062140//201712071050--201712081733//201712081807--201712092037//201712110910--201712120034//201712121717--201712131623//
        # 201712140910----201712141808//
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=greenhouse+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=growing+light+greenhouse',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=indoor+farming+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=indoor+garden+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=led+plant+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=plant+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=smart+garden+grow+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=grow+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=flowering+led+grow+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=grow+light+flowering',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=full+spectrum+led+grow+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=greenhouse+grow+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=grow+bulbs+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=grow+light+full+cycle',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=greenhouse+light+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=grow+led+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=grow+light+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=grow+light+bulb+for+indoor+plants',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=grow+light+bulb+led',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=grow+light+vegetative',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=grow+lights+bulbs',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=grow+lights+for+indoor+plants',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=hydroponics+led+grow+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=indoor+grow+lights+for+plants',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=indoor+led+grow+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=indoor+plant+grow+lights',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=indoor+plant+light+led',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=led+grow+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=led+grow+light+bulb',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=led+grow+lights+for+indoor+plants',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=led+plant+light',
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=led+plant+lights+for+indoor+plants',
        # 'https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=plant+grow+lights+indoor',
        # 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=plant+light+bulb',
        # # 智能灯//20171114//201711151821-201711160900//201711171812--201711201400//201711220915--201711231800//201711232026--201711240233//
        # 201712060910--201712062140//201712081807--201712092037//201712110910--201712120034//201712120930--201712121710//
        # 201712140910----201712141808//
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
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=dimmable+led+bulbs',
        # A48系列//20171114//201711160915-201711170900//201711171812--201711201400//201711220915--201711231800//201711232026--
        # 201712070915--201712071036//201712081807--201712092037//201712110910--201712120034//201712120930--201712121710//
        # 201712140910--201712141808//
        'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=60w+led+bulb',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=40w+led+bulb',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=3000k+led+bulb',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=a15+led+bulb+60w',
        'https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=led+light+bulbs',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=40+watt+light+bulbs+led',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=cool+white+led+bulb',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=e26+bulb+40+watt',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=60w+light+bulb',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=60watt+light+bulb',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=40w+led+bulb+soft+white',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=40w+led+light+bulbs',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=60+watt+light+bulb',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=A15+led+bulb',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=a15+led+bulb+daylight',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=ceramic+led+bulb',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=led+40w+equivalent',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=LED+40W+light+bulbs',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=led+light+bulbs+40',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=warm+white+led+bulb',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=daylight+led+bulb',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=e26+led+bulb+40w',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=60w+led+bulb+dimmable',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=e26+60w+led+bulb',
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=led+bulb+60w',
    ]

    custom_settings = {
        'RETRY_TIMES': 100,
        'DOWNLOAD_DELAY': 0.5,
        'ITEM_PIPELINES': {
            'collect_email.pipelines.UserEmailPipeline': 1
        }
    }

    url_pre = 'https://www.amazon.com/product-reviews/'
    url_endding = '/ref=cm_cr_arp_d_show_all?ie=UTF8&reviewerType=all_reviews&pageNumber=1'
    # 20170919    # has_email_index = 26076    # 20171018    # has_email_index = 29927    # 20171102    # has_email_index = 36014    # 20171106    # has_email_index = 40516
    # 20171108    # has_email_index = 45042    # 20171109    # has_email_index = 46885    # 20171110    # has_email_index = 50908    # 20171114    # has_email_index = 53149
    # 20171115    # has_email_index = 54056    # 20171115    # has_email_index = 57461    # 20171116    # has_email_index = 59821    # 20171117    # has_email_index = 62392
    # 20171117    # has_email_index = 64029    # 20171121    # has_email_index = 67575    # 20171122    # has_email_index = 70313    # 20171123    # has_email_index = 73536
    # 20171205    # has_email_index = 74554    # 20171206    # has_email_index = 77006    # 20171207    # has_email_index = 79249    # 20171207    # has_email_index = 79486
    # 20171208    # has_email_index = 82654    # 20171211    # has_email_index = 85959    # 20171212    # has_email_index = 88179    # 20171212    # has_email_index = 89418
    # 20171213    # has_email_index = 92158    # 20171214    # has_email_index = 92239

    has_email_index = session.query(func.max(UserEmails.index)).all()[0][0]

    all_user_index = 0

    ASINs_list = session.query(AsinKeyword.asin).distinct().all()
    ASIN_Keyword_list = session.query(AsinKeyword.asin, AsinKeyword.keyword).all()
    Distinct_email_list = session.query(UserEmails.email).distinct().all()
    Distinct_email_count = len(Distinct_email_list)
    New_eamil_count = 0
    New_distinct_eamil_count = 0.0
    New_distinct_email_rate = 0.0
    ATCOOE = 0
    ATCOODE = 0
    # error_index = session.query(func.max(AsinOfError.id)).all()[0][0];

    # print(ASINs_list)
    # print(ASIN_Keyword_list)

    ASIN_Keyword_index = session.query(func.max(AsinKeyword.index)).all()[0][0]

    total_time_start = time.time()
    single_time_start = time.time()

    def parse(self, response):
        meta = dict()
        meta['keyword'] = response.url.split('keywords=')[1].split('&')[0]

        if 'page=' in response.url:
            product_at_page = response.url.split('page=')[1].split('&')[0]
        else:
            product_at_page = 1

        meta['product_at_page'] = product_at_page


        # //li[contains(@class, 's-result-item')]
        # allProductLink = response.xpath('//ul[@id="s-results-list-atf"]/li')
        # allProductLink = response.xpath('//li[contains(@class, "s-result-item")]')
        allProductLink = response.xpath('//ul[contains(@class, "s-result-list")]/li')
        for item in allProductLink:
            asin = item.xpath('@data-asin').extract_first()
            print(asin, '|| product count of this page:', len(allProductLink))
            li_id = item.xpath('@id').extract_first()
            comment_page_url = self.url_pre + asin + self.url_endding
            meta['product_index'] = li_id

            if (asin,) in self.ASINs_list:
                print('\n--------------------------', asin, u'This Product has been searched--------------------------\n\n')
                print('||', u'New Distinct Email Count: %d' % self.New_distinct_eamil_count)
                print('CURRENT DISTINCT EMAILS COUNT :', self.Distinct_email_count + self.New_distinct_eamil_count)

                if (asin, meta['keyword']) in self.ASIN_Keyword_list:
                    pass
                else:
                    print('\n--------------------------', asin, u'Add new keyword to this product', meta['keyword'], '--------------------------\n\n')
                    self.ASIN_Keyword_list.append((asin, meta['keyword']))
                    self.ASIN_Keyword_index = self.ASIN_Keyword_index + 1
                    asin_keyword_item = AsinKeywordItem()
                    asin_keyword_item['index'] = self.ASIN_Keyword_index
                    asin_keyword_item['asin'] = asin
                    asin_keyword_item['keyword'] = meta['keyword']
                    yield asin_keyword_item
            else:
                print('\n--------------------------', asin, u'NEW PRODUCT !!!--------------------------\n\n')
                self.ASINs_list.append((asin,))
                self.ASIN_Keyword_list.append((asin, meta['keyword']))
                self.ASIN_Keyword_index = self.ASIN_Keyword_index + 1
                asin_keyword_item = AsinKeywordItem()
                asin_keyword_item['index'] = self.ASIN_Keyword_index
                asin_keyword_item['asin'] = asin
                asin_keyword_item['keyword'] = meta['keyword']
                yield asin_keyword_item

                yield scrapy.Request(comment_page_url, callback=self.parse_comment_page, meta=meta)


        url = response.xpath('//a[@id="pagnNextLink"]/@href').extract_first()

        if url:
            page = "https://www.amazon.com" + url
            yield scrapy.Request(page, callback=self.parse)
        else:
            print('All Products have been searched !!!')

    def parse_comment_page(self, response):
        product_at_page = response.meta['product_at_page']
        product_index = response.meta['product_index']
        keyword = response.meta['keyword']

        meta_to_parse_comment_page = dict()
        meta_to_parse_comment_page['product_at_page'] = product_at_page
        meta_to_parse_comment_page['product_index'] = product_index
        meta_to_parse_comment_page['keyword'] = keyword

        meta = dict()
        product_asin = response.url.split('product-reviews/')[1].split('/')[0].split('?')[0]
        meta['product_asin'] = product_asin
        meta['product_at_page'] = product_at_page
        meta['product_index'] = product_index
        meta['keyword'] = keyword

        base_url = 'https://www.amazon.com'

        allUserLink = response.xpath('//div[@data-hook = "review"]/div')
        print('/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/')
        print("user link of one page:", len(allUserLink))
        print('/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/')

        for item in allUserLink:
            username = item.xpath('./div[2]//a[@data-hook = "review-author"]/text()').extract_first()
            userurl = base_url + item.xpath('./div[2]//a[@data-hook = "review-author"]/@href').extract_first()
            stars = float(item.xpath('./div/a[@class = "a-link-normal"]/@title').extract_first().split(' ')[0])
            meta['stars'] = stars
            meta['username'] = username


            yield scrapy.Request(userurl, callback=self.parse_user_page, cookies=self.cookie, meta=meta, headers=self.headers)

        url = response.xpath('//li[@class="a-last"]/a/@href').extract_first()

        if url:
            page = "https://www.amazon.com" + url
            yield scrapy.Request(page, callback=self.parse_comment_page, meta=meta_to_parse_comment_page)
        else:
            pass

    def parse_user_page(self, response):
        product_asin = response.meta['product_asin']
        product_at_page = response.meta['product_at_page']
        product_index = response.meta['product_index']
        stars = response.meta['stars']
        user_name = response.meta['username']
        keyword = response.meta['keyword']

        response_text = response.body.decode('utf-8')

        self.all_user_index = self.all_user_index + 1

        if 'maitiantian' in response_text:
            if '"publicEmail":null' in response_text:
                print('\n--------------------------', 'No.', self.all_user_index, 'NO USER EMAIL--------------------------')
                user_email = 'null'

                print('USERNAME :', user_name)
                print('USER EMAIL :', user_email)
                print('KEYWORD :', keyword)
                # print('PRODUCT INDEX :', product_index)
                print('PRODUCT ASIN :', product_asin)
                print('USER REVIEW STARS :', stars)
                # print('PRODUCT AT SEARCH PAGE :', product_at_page)
                print('CURRENT DISTINCT EMAILS COUNT :', self.Distinct_email_count + self.New_distinct_eamil_count)
                print('------------------------------------------------------------------------')

                now = time.time()
                total_time = now - self.total_time_start
                single_time = now - self.single_time_start
                self.single_time_start = total_time + self.total_time_start

                print('||', u'Time of this search : %.3fs' % single_time)
                print('||', u'Time of all search  : %.3fs' % total_time)
                print('-----------------------------------')
                if self.New_eamil_count == 0:
                    pass
                else:
                    self.ATCOOE = total_time / self.New_eamil_count
                    if self.New_distinct_eamil_count == 0:
                        pass
                    else:
                        self.ATCOODE = total_time / self.New_distinct_eamil_count
                print('||', u'New Email Count: %d' % self.New_eamil_count)
                print('||', u'New Distinct Email Count: %d' % self.New_distinct_eamil_count)
                print('||', u'Average time cost of one email: %.3fs' % self.ATCOOE)
                print('||', u'Average time cost of one DISTINCT email: %.3fs' % self.ATCOODE)
                print('||', u'New DISTINCT email Rate: %.2f' % self.New_distinct_email_rate + u'%')
                print('-----------------------------------\n\n')
            else:
                print('\n--------------------------', 'No.', self.all_user_index, 'THERE IS AN EMAIL--------------------------')
                user_email = response_text.split('"publicEmail":"')[1].split('"')[0]

                now = time.time()
                total_time = now - self.total_time_start
                single_time = now - self.single_time_start
                self.single_time_start = total_time + self.total_time_start

                if (user_email,) in self.Distinct_email_list:
                    self.New_eamil_count = self.New_eamil_count + 1
                    self.ATCOOE = total_time/self.New_eamil_count
                    self.New_distinct_email_rate = self.New_distinct_eamil_count/self.New_eamil_count*100
                else:
                    self.Distinct_email_list.append((user_email,))
                    self.New_eamil_count = self.New_eamil_count + 1
                    self.ATCOOE = total_time/self.New_eamil_count
                    self.New_distinct_eamil_count = self.New_distinct_eamil_count + 1
                    self.ATCOODE = total_time/self.New_distinct_eamil_count
                    self.New_distinct_email_rate = self.New_distinct_eamil_count/self.New_eamil_count*100

                self.has_email_index = self.has_email_index + 1

                print('INDEX :', self.has_email_index)
                print('USERNAME :', user_name)
                print('USER EMAIL :', user_email)
                print('KEYWORD :', keyword)
                # print('PRODUCT INDEX :', product_index)
                print('PRODUCT ASIN :', product_asin)
                print('USER REVIEW STARS :', stars)
                # print('PRODUCT AT SEARCH PAGE :', product_at_page)
                print('CURRENT DISTINCT EMAILS COUNT :', self.Distinct_email_count + self.New_distinct_eamil_count)
                print('------------------------------------------------------------------------')

                item = UserEmailItem()
                item['index'] = self.has_email_index
                item['username'] = user_name
                item['email'] = user_email
                item['asin'] = product_asin
                item['stars'] = stars
                item['product_at_page'] = product_at_page
                item['product_index'] = product_index
                item['keyword'] = keyword

                print('||', u'Time of this search : %.3fs' % single_time)
                print('||', u'Time of all search  : %.3fs' % total_time)
                print('-----------------------------------')
                print('||', u'New Email Count: %d' % self.New_eamil_count)
                print('||', u'New Distinct Email Count: %d' % self.New_distinct_eamil_count)
                print('||', u'Average time cost of one email: %.3fs' % self.ATCOOE)
                print('||', u'Average time cost of one DISTINCT email: %.3fs' % self.ATCOODE)
                print('||', u'New DISTINCT email Rate: %.2f' % self.New_distinct_email_rate + u'%')
                print('-----------------------------------\n\n')

                yield item


        else:
            print('\n--------------------------', 'No.', self.all_user_index, 'ERROR--------------------------')
            # error_index = session.query(func.max(AsinOfError.id)).all()[0][0];
            item = AsinOfErrorItem()
            # self.error_index = self.error_index + 1
            # item['id'] = self.error_index
            # item['asin'] = product_asin
            # item['keyword'] = keyword
            item['asin_keyword'] = product_asin + '|' + keyword
            item['redo'] = 0

            try:
                yield item
            except:
                print('this asin_keyword already exist !')

            # yield item

            print(u'$%#$%#$%#$%#$%    You are not login yet!    $%#$%#$%#$%#$%')
            print('-----------------------------------------------------------------\n')
