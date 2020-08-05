import scrapy
from ..items  import AmznTutItem


class MultiPageSpider(scrapy.Spider):
    name = 'multi_page'
    #allowed_domains = ['amazon.com']
    page_number = 2
    start_urls = [
        'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1596369127&rnid=1250225011&ref=lp_283155_nr_p_n_publication_date_0'
    ]

    def parse(self, response):
        items = AmznTutItem()
        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_author = response.css('.sg-col-12-of-28 .a-size-base+ .a-size-base').css('::text').extract()
        product_price = response.css('.a-spacing-top-small .a-price span span').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items


        next_page = 'https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page=' + str(MultiPageSpider.page_number) + '&fst=as%3Aoff&qid=1596541318&rnid=1250225011&ref=sr_pg_2'
        if MultiPageSpider.page_number <=75:
            MultiPageSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)