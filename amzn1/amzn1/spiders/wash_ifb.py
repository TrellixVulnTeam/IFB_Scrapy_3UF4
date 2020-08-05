import scrapy
from ..items import Amzn1Item

class WashIfbSpider(scrapy.Spider):
    name = 'wash_ifb'
    #allowed_domains = ['amazon.in']

    start_urls = [
      "https://amazon.in/IFB-Fully-Automatic-Diva-Aqua-SX/dp/B071G3B81W/ref=sr_1_1?dchild=1&fst=as%3Aoff&qid=1596560778&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-1",
      "https://amazon.in/IFB-Fully-Automatic-Loading-Senator-WXS/dp/B07MFPKX4W/ref=sr_1_2?dchild=1&fst=as%3Aoff&qid=1596560778&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-2",
      "https://amazon.in/IFB-Fully-Automatic-Serena-Aqua-SXA/dp/B07DZTY1QK/ref=sr_1_3?dchild=1&fst=as%3Aoff&qid=1596560778&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-3",
      "https://amazon.in/IFB-Fully-Automatic-TL-RDW-6-5kg-Aqua/dp/B00WU9Z040/ref=sr_1_4?dchild=1&fst=as%3Aoff&qid=1596560778&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-4",
      "https://amazon.in/IFB-Fully-Automatic-TL-RDS-Aqua-Sparkling/dp/B00WU9Z51I/ref=sr_1_5?dchild=1&fst=as%3Aoff&qid=1596560778&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-5",
      "https://amazon.in/IFB-Fully-Automatic-TL-SGDG-7-0Kg-AQUA/dp/B00WU9Z9F0/ref=sr_1_6?dchild=1&fst=as%3Aoff&qid=1596560778&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-6",
      "https://amazon.in/IFB-Fully-Automatic-TL-RCG-RCSG-Aqua/dp/B00WUA0486/ref=sr_1_7?dchild=1&fst=as%3Aoff&qid=1596560778&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-7",
      "https://amazon.in/IFB-Dryer-Dry-EX-Silver/dp/B00RE6RL8M/ref=sr_1_8?dchild=1&fst=as%3Aoff&qid=1596560778&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-8",
      "https://amazon.in/IFB-Fully-Automatic-Loading-Elite-WX/dp/B078JJ6C8B/ref=sr_1_9?dchild=1&fst=as%3Aoff&qid=1596560778&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-9",
      "https://amazon.in/IFB-Fully-Automatic-Loading-Serena-WX/dp/B078JJHK6Q/ref=sr_1_10?dchild=1&fst=as%3Aoff&qid=1596560778&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-10",
      "https://amazon.in/IFB-Fully-Automatic-Loading-Senorita-WXS/dp/B07BNT389H/ref=sr_1_11?dchild=1&fst=as%3Aoff&qid=1596560778&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-11",
      "https://amazon.in/IFB-Fully-Automatic-Loading-ELENA-ZXS/dp/B07XVNTR6J/ref=sr_1_12?dchild=1&fst=as%3Aoff&qid=1596560778&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-12",
      "https://amazon.in/IFB-Fully-Automatic-Loading-Elena-ZX/dp/B07WMJMNWJ/ref=sr_1_13?dchild=1&fst=as%3Aoff&qid=1596560778&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-13",
      "https://amazon.in/IFB-6-5-Fully-Automatic-SENORITA-ZX/dp/B07RXHWL6R/ref=sr_1_14?dchild=1&fst=as%3Aoff&qid=1596560778&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-14",
      "https://amazon.in/IFB-Fully-automatic-Top-loading-Washing-Graphite/dp/B00WU9ZYMS/ref=sr_1_15?dchild=1&fst=as%3Aoff&qid=1596560778&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-15",
      "https://amazon.in/IFB-Fully-Automatic-Loading-Senorita-WX/dp/B078JJTY8Q/ref=sr_1_16?dchild=1&fst=as%3Aoff&qid=1596560778&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-16",
      "https://amazon.in/IFB-Fully-Automatic-Loading-EVA-ZXS/dp/B07XVNLX9Y/ref=sr_1_17?dchild=1&fst=as%3Aoff&qid=1596599663&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-17",
      "https://amazon.in/IFB-Fully-Automatic-Loading-6-5KG-AQUA/dp/B00WUA08SW/ref=sr_1_18?dchild=1&fst=as%3Aoff&qid=1596599663&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-18",
      "https://amazon.in/IFB-10-5-Fully-Automatic-TL-SDIN/dp/B0856FTBRN/ref=sr_1_19?dchild=1&fst=as%3Aoff&qid=1596599663&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-19",
      "https://amazon.in/IFB-SX-Fully-automatic-Front-loading-Washing/dp/B01AJO3PWG/ref=sr_1_20?dchild=1&fst=as%3Aoff&qid=1596599663&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-20",
      "https://amazon.in/IFB-Fully-Automatic-Loading-Washing-NEODIVA-SX/dp/B07XVP3BBL/ref=sr_1_21?dchild=1&fst=as%3Aoff&qid=1596599663&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-21",
      "https://amazon.in/IFB-Fully-Automatic-Loading-Washing-NEODIVA-VX/dp/B07XLSCXQ8/ref=sr_1_22?dchild=1&fst=as%3Aoff&qid=1596599663&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-22",
      "https://amazon.in/IFB-Fully-Automatic-Loading-ELITE-ZXS/dp/B07XVNZZBD/ref=sr_1_23?dchild=1&fst=as%3Aoff&qid=1596599663&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-23",
      "https://amazon.in/IFB-Fully-Automatic-Loading-EVA-ZX/dp/B07WHLQYJG/ref=sr_1_24?dchild=1&fst=as%3Aoff&qid=1596599663&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-24",
      "https://amazon.in/IFB-6-5-Fully-Automatic-TL-Aqua/dp/B01H1Z5FZ6/ref=sr_1_25?dchild=1&fst=as%3Aoff&qid=1596599663&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-25",
      "https://amazon.in/IFB-Fully-Automatic-TL-SSBL-8-5KG-AQUA/dp/B07XLSDF2P/ref=sr_1_26?dchild=1&fst=as%3Aoff&qid=1596599663&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-26",
      "https://amazon.in/IFB-Fully-Automatic-Diva-Aqua-softener/dp/B082Q58W5V/ref=sr_1_27?dchild=1&fst=as%3Aoff&qid=1596599663&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-27",
      "https://amazon.in/IFB-Fully-Automatic-TL-SDBR-8-5KG-AQUA/dp/B07XVNFY2H/ref=sr_1_28?dchild=1&fst=as%3Aoff&qid=1596599663&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-28",
      "https://amazon.in/IFB-Fully-Automatic-TL-RCH-Aqua-Champagne/dp/B00WU9ZDS8/ref=sr_1_29?dchild=1&fst=as%3Aoff&qid=1596599663&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-29",
      "https://amazon.in/IFB-Fully-Automatic-ELENA-PLUS-ZX/dp/B07XVVJ2RZ/ref=sr_1_30?dchild=1&fst=as%3Aoff&qid=1596599663&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-30",
      "https://amazon.in/IFB-TL85SCH-Fully-automatic-Top-loading-Champagne/dp/B00WU9ZU7M/ref=sr_1_31?dchild=1&fst=as%3Aoff&qid=1596599663&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-31",
      "https://amazon.in/IFB-Fully-Automatic-TL-RDW-6-5kg-softener/dp/B082Q192Q8/ref=sr_1_32?dchild=1&fst=as%3Aoff&qid=1596599663&refinements=p_89%3AIFB&rnid=3837712031&s=kitchen&sr=1-32"
    ]

    def parse(self, response):
        items = Amzn1Item()
        product_name = response.xpath('//*[(@id = "productTitle")]/text()').extract()
        product_rating = response.css('.a-size-medium.a-color-base').css('::text').extract()
        #a-size-medium a-color-base a-text-beside-button a-text-bold
        product_price = response.xpath('//*[(@id = "priceblock_ourprice")]/text()').extract()

        #cleaning text
        names = [item.strip('\n') for item in product_name]
        prices = [item.strip('\u20b9\xa0') for item in product_price]
        rating = [item.strip(' out of 5') for item in product_rating]

        items['product_name'] = names
        items['product_rating'] = rating
        items['product_price'] = prices


        yield items