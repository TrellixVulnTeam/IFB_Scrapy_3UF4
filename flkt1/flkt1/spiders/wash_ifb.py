import scrapy
from ..items import Flkt1Item

class WashIfbSpider(scrapy.Spider):
    name = 'wash_ifb'
    #allowed_domains = ['flipkart.com']
    start_urls = [
      "https://flipkart.com/ifb-8-kg-fully-automatic-top-load-grey/p/itmff6xkazexwmy3?pid=WMNECJTGHCQWCAXY&lid=LSTWMNECJTGHCQWCAXY8RSQ4G&marketplace=FLIPKART&srno=b_2_25&otracker=CLP_Filters&fm=organic&iid=b775ac81-b9c5-4f00-93f0-d39c6fbbe459.WMNECJTGHCQWCAXY.SEARCH&ssid=5bzrqhiai80000001596626729423",
      "https://flipkart.com/ifb-6-5-kg-fully-automatic-top-load-grey/p/itmejfggbfwf9qjd?pid=WMNEJFGGCXGZCUZK&lid=LSTWMNEJFGGCXGZCUZKJAB2HW&marketplace=FLIPKART&srno=b_2_26&otracker=CLP_Filters&fm=organic&iid=b775ac81-b9c5-4f00-93f0-d39c6fbbe459.WMNEJFGGCXGZCUZK.SEARCH&ssid=5bzrqhiai80000001596626729423",
      "https://flipkart.com/ifb-7-kg-fully-automatic-top-load-white/p/itmew6qszdpzhz94?pid=WMNEW6QS6HE7XDHZ&lid=LSTWMNEW6QS6HE7XDHZ8TVR3M&marketplace=FLIPKART&srno=b_2_27&otracker=CLP_Filters&fm=organic&iid=b775ac81-b9c5-4f00-93f0-d39c6fbbe459.WMNEW6QS6HE7XDHZ.SEARCH&ssid=5bzrqhiai80000001596626729423",
      "https://flipkart.com/ifb-6-5-kg-fully-automatic-front-load-in-built-heater-white/p/itmezw2mzez8zume?pid=WMNEZW2MTEYTVHHH&lid=LSTWMNEZW2MTEYTVHHHVJVWSZ&marketplace=FLIPKART&srno=b_2_28&otracker=CLP_Filters&fm=organic&iid=b775ac81-b9c5-4f00-93f0-d39c6fbbe459.WMNEZW2MTEYTVHHH.SEARCH&ssid=5bzrqhiai80000001596626729423",
      "https://flipkart.com/ifb-7-5-kg-fully-automatic-front-load-in-built-heater-white/p/itmezw2mugmjdhgy?pid=WMNEZW2M4CJHSJ23&lid=LSTWMNEZW2M4CJHSJ23JS427J&marketplace=FLIPKART&srno=b_2_29&otracker=CLP_Filters&fm=organic&iid=b775ac81-b9c5-4f00-93f0-d39c6fbbe459.WMNEZW2M4CJHSJ23.SEARCH&ssid=5bzrqhiai80000001596626729423",
      "https://flipkart.com/ifb-7-5-kg-fully-automatic-front-load-in-built-heater-white/p/itmfcf8hgbgzuwpz?pid=WMNFCF8HCVNN77Z6&lid=LSTWMNFCF8HCVNN77Z6WOPW80&marketplace=FLIPKART&srno=b_2_30&otracker=CLP_Filters&fm=organic&iid=b775ac81-b9c5-4f00-93f0-d39c6fbbe459.WMNFCF8HCVNN77Z6.SEARCH&ssid=5bzrqhiai80000001596626729423",
      "https://flipkart.com/ifb-7-5-kg-fully-automatic-top-load-silver/p/itmequmthpv78hjh?pid=WMNEQUMTFAGJTGTB&lid=LSTWMNEQUMTFAGJTGTBFRMHZW&marketplace=FLIPKART&srno=b_2_31&otracker=CLP_Filters&fm=organic&iid=b775ac81-b9c5-4f00-93f0-d39c6fbbe459.WMNEQUMTFAGJTGTB.SEARCH&ssid=5bzrqhiai80000001596626729423",
      "https://flipkart.com/ifb-6-kg-fully-automatic-front-load-in-built-heater-silver/p/itmewfs4bdqjd8gd?pid=WMNEWFS4SHWDPGEA&lid=LSTWMNEWFS4SHWDPGEACC042J&marketplace=FLIPKART&srno=b_2_32&otracker=CLP_Filters&fm=organic&iid=b775ac81-b9c5-4f00-93f0-d39c6fbbe459.WMNEWFS4SHWDPGEA.SEARCH&ssid=5bzrqhiai80000001596626729423",
      "https://flipkart.com/ifb-6-kg-fully-automatic-front-load-in-built-heater-silver/p/itmedkrgghtrasys?pid=WMNEDKRG5EHZAMYN&lid=LSTWMNEDKRG5EHZAMYNFJKKWG&marketplace=FLIPKART&srno=b_2_33&otracker=CLP_Filters&fm=organic&iid=b775ac81-b9c5-4f00-93f0-d39c6fbbe459.WMNEDKRG5EHZAMYN.SEARCH&ssid=5bzrqhiai80000001596626729423",
      "https://flipkart.com/ifb-7-kg-fully-automatic-front-load-in-built-heater-silver/p/itmdy9svbbzqax9d?pid=WMNDY9RWWMPRYZZG&lid=LSTWMNDY9RWWMPRYZZGNXAVXB&marketplace=FLIPKART&srno=b_2_34&otracker=CLP_Filters&fm=organic&iid=b775ac81-b9c5-4f00-93f0-d39c6fbbe459.WMNDY9RWWMPRYZZG.SEARCH&ssid=5bzrqhiai80000001596626729423",
      "https://flipkart.com/ifb-6-kg-fully-automatic-front-load-in-built-heater-silver/p/itmdy9svmra86qsu?pid=WMNDY9RWCFTDBHH4&lid=LSTWMNDY9RWCFTDBHH4IAJDJK&marketplace=FLIPKART&srno=b_2_35&otracker=CLP_Filters&fm=organic&iid=b775ac81-b9c5-4f00-93f0-d39c6fbbe459.WMNDY9RWCFTDBHH4.SEARCH&ssid=5bzrqhiai80000001596626729423",
      "https://flipkart.com/ifb-6-5-kg-fully-automatic-front-load-in-built-heater-white/p/itme7dcq3pssheb2?pid=WMNDY9RWYSV7AWUH&lid=LSTWMNDY9RWYSV7AWUHSYSC2S&marketplace=FLIPKART&srno=b_2_36&otracker=CLP_Filters&fm=organic&iid=b775ac81-b9c5-4f00-93f0-d39c6fbbe459.WMNDY9RWYSV7AWUH.SEARCH&ssid=5bzrqhiai80000001596626729423",
      "https://flipkart.com/ifb-6-5-kg-fully-automatic-front-load-in-built-heater-silver/p/itmezqjyhgxnhmfd?pid=WMNEZQJYSEPRBJHJ&lid=LSTWMNEZQJYSEPRBJHJMXX9KX&marketplace=FLIPKART&srno=b_2_37&otracker=CLP_Filters&fm=organic&iid=b775ac81-b9c5-4f00-93f0-d39c6fbbe459.WMNEZQJYSEPRBJHJ.SEARCH&ssid=5bzrqhiai80000001596626729423",
      "https://flipkart.com/ifb-8-kg-fully-automatic-top-load-silver/p/itmecjtgb7ghur77?pid=WMNEJFGGTTG7TPK8&lid=LSTWMNEJFGGTTG7TPK8XQASNJ&marketplace=FLIPKART&srno=b_2_38&otracker=CLP_Filters&fm=organic&iid=b775ac81-b9c5-4f00-93f0-d39c6fbbe459.WMNEJFGGTTG7TPK8.SEARCH&ssid=5bzrqhiai80000001596626729423",
      "https://flipkart.com/ifb-6-5-kg-fully-automatic-front-load-in-built-heater-white/p/itmexgyjaybz3zb9?pid=WMNEXGYJKKQYDGED&lid=LSTWMNEXGYJKKQYDGEDOV3BL0&marketplace=FLIPKART&srno=b_2_39&otracker=CLP_Filters&fm=organic&iid=b775ac81-b9c5-4f00-93f0-d39c6fbbe459.WMNEXGYJKKQYDGED.SEARCH&ssid=5bzrqhiai80000001596626729423",
      "https://flipkart.com/ifb-7-kg-fully-automatic-front-load-in-built-heater-white/p/itme8g53jeffatyu?pid=WMNE8G53DMNVJAG8&lid=LSTWMNE8G53DMNVJAG8N1UKGC&marketplace=FLIPKART&srno=b_2_40&otracker=CLP_Filters&fm=organic&iid=b775ac81-b9c5-4f00-93f0-d39c6fbbe459.WMNE8G53DMNVJAG8.SEARCH&ssid=5bzrqhiai80000001596626729423",
      "https://flipkart.com/ifb-6-kg-fully-automatic-front-load-in-built-heater-white/p/itme7n447yrbtzam?pid=WMNE7N446GD8HH7G&lid=LSTWMNE7N446GD8HH7GR5PGRT&marketplace=FLIPKART&srno=b_2_41&otracker=CLP_Filters&fm=organic&iid=b775ac81-b9c5-4f00-93f0-d39c6fbbe459.WMNE7N446GD8HH7G.SEARCH&ssid=5bzrqhiai80000001596626729423",
      "https://flipkart.com/ifb-8-kg-5-star-fully-automatic-front-load-in-built-heater-silver/p/itm3c3e4cc03210a?pid=WMNFTQHGHANFRZCM&lid=LSTWMNFTQHGHANFRZCMNP1HDH&marketplace=FLIPKART&srno=b_2_42&otracker=CLP_Filters&fm=organic&iid=b775ac81-b9c5-4f00-93f0-d39c6fbbe459.WMNFTQHGHANFRZCM.SEARCH&ssid=5bzrqhiai80000001596626729423",
      "https://flipkart.com/ifb-8-5-kg-fully-automatic-top-load-in-built-heater-brown/p/itm92840803dd99b?pid=WMNFQGYUAQJRYJGN&lid=LSTWMNFQGYUAQJRYJGNKRVYL3&marketplace=FLIPKART&srno=b_2_43&otracker=CLP_Filters&fm=organic&iid=b775ac81-b9c5-4f00-93f0-d39c6fbbe459.WMNFQGYUAQJRYJGN.SEARCH&ssid=5bzrqhiai80000001596626729423",
      "https://flipkart.com/ifb-6-kg-2d-wash-fully-automatic-front-load-in-built-heater-white/p/itmehpcrfmzed87b?pid=WMNEHPCR5BJHXPRT&lid=LSTWMNEHPCR5BJHXPRTTAVXAI&marketplace=FLIPKART&srno=b_1_1&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNEHPCR5BJHXPRT.SEARCH&ssid=z05xatsz5s0000001596626729474",
      "https://flipkart.com/ifb-6-5-kg-water-softener-aqua-energie-fully-automatic-top-load-white/p/itm013b0ee61f7a7?pid=WMNFNWJ8SRWH7PKN&lid=LSTWMNFNWJ8SRWH7PKN0PABD7&marketplace=FLIPKART&srno=b_1_2&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNFNWJ8SRWH7PKN.SEARCH&ssid=z05xatsz5s0000001596626729474",
      "https://flipkart.com/ifb-7-kg-2d-wash-self-diagnosis-fully-automatic-front-load-in-built-heater-silver/p/itm30d3aa51a76c9?pid=WMNF2P7YGZMXEFVK&lid=LSTWMNF2P7YGZMXEFVKPHJUKA&marketplace=FLIPKART&srno=b_1_3&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNF2P7YGZMXEFVK.SEARCH&ssid=z05xatsz5s0000001596626729474",
      "https://flipkart.com/ifb-8-kg-unbalance-correction-self-diagnosis-fully-automatic-front-load-in-built-heater-silver/p/itmfb29mz7fw8mzf?pid=WMNFB29MBFKQKUG6&lid=LSTWMNFB29MBFKQKUG65EBUP0&marketplace=FLIPKART&srno=b_1_4&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNFB29MBFKQKUG6.SEARCH&ssid=z05xatsz5s0000001596626729474",
      "https://flipkart.com/ifb-6-kg-fully-automatic-front-load-in-built-heater-silver/p/itm5f9e641100f09?pid=WMNFJY5UCJHHFQWC&lid=LSTWMNFJY5UCJHHFQWC75TE27&marketplace=FLIPKART&srno=b_1_5&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNFJY5UCJHHFQWC.SEARCH&ssid=z05xatsz5s0000001596626729474",
      "https://flipkart.com/ifb-6-5-kg-water-softener-aqua-energie-auto-imbalance-fully-automatic-top-load-silver/p/itme7n44fajwgxh2?pid=WMNE7N442RHHWA8Z&lid=LSTWMNE7N442RHHWA8ZLM3OIR&marketplace=FLIPKART&srno=b_1_6&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNE7N442RHHWA8Z.SEARCH&ssid=z05xatsz5s0000001596626729474",
      "https://flipkart.com/ifb-6-5-kg-fully-automatic-front-load-in-built-heater-silver/p/itmfgu8vzfqebhvf?pid=WMNFGU8VPXNRCU6H&lid=LSTWMNFGU8VPXNRCU6HTJZRKS&marketplace=FLIPKART&srno=b_1_7&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNFGU8VPXNRCU6H.SEARCH&ssid=z05xatsz5s0000001596626729474",
      "https://flipkart.com/ifb-7-kg-fully-automatic-top-load-grey/p/itmf2gbw9ud6vb6k?pid=WMNECJTGHTYZHYTH&lid=LSTWMNECJTGHTYZHYTHTDZJ6Y&marketplace=FLIPKART&srno=b_1_8&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNECJTGHTYZHYTH.SEARCH&ssid=z05xatsz5s0000001596626729474",
      "https://flipkart.com/ifb-8-5-kg-fully-automatic-front-load-in-built-heater-white/p/itmezw2mxa74pacb?pid=WMNEZW2MZEFZYMCY&lid=LSTWMNEZW2MZEFZYMCYKBMDFB&marketplace=FLIPKART&srno=b_1_9&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNEZW2MZEFZYMCY.SEARCH&ssid=z05xatsz5s0000001596626729474",
      "https://flipkart.com/ifb-7-kg-fully-automatic-front-load-in-built-heater-silver/p/itm1ee10048d83a7?pid=WMNFJY5UX7MJHV9H&lid=LSTWMNFJY5UX7MJHV9HK4EBUD&marketplace=FLIPKART&srno=b_1_10&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNFJY5UX7MJHV9H.SEARCH&ssid=z05xatsz5s0000001596626729474",
      "https://flipkart.com/ifb-6-5-kg-fully-automatic-front-load-in-built-heater-white/p/itmfgu8vuktydd2s?pid=WMNFGU8VDGCW3FCC&lid=LSTWMNFGU8VDGCW3FCCBJX7CW&marketplace=FLIPKART&srno=b_1_11&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNFGU8VDGCW3FCC.SEARCH&ssid=z05xatsz5s0000001596626729474",
      "https://flipkart.com/ifb-6-5-kg-fully-automatic-top-load-red/p/itme7n44adtxghgs?pid=WMNE7N44Y3JTGNZW&lid=LSTWMNE7N44Y3JTGNZWPUY8R8&marketplace=FLIPKART&srno=b_1_12&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNE7N44Y3JTGNZW.SEARCH&ssid=z05xatsz5s0000001596626729474",
      "https://flipkart.com/ifb-6-kg-fully-automatic-front-load-in-built-heater-white/p/itm976ebbb365ea3?pid=WMNFJY5UWW3F2EZC&lid=LSTWMNFJY5UWW3F2EZCHLPWKW&marketplace=FLIPKART&srno=b_1_13&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNFJY5UWW3F2EZC.SEARCH&ssid=z05xatsz5s0000001596626729474",
      "https://flipkart.com/ifb-6-kg-fully-automatic-front-load-in-built-heater-silver/p/itmfgu8v7wgb2hqg?pid=WMNFJY5UTBQBBRV5&lid=LSTWMNFJY5UTBQBBRV5DLR7BG&marketplace=FLIPKART&srno=b_1_14&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNFJY5UTBQBBRV5.SEARCH&ssid=z05xatsz5s0000001596626729474",
      "https://flipkart.com/ifb-6-kg-fully-automatic-front-load-in-built-heater-white/p/itmfgu8vuemv9prr?pid=WMNFGU8VYKM65HSN&lid=LSTWMNFGU8VYKM65HSNFHIU0B&marketplace=FLIPKART&srno=b_1_15&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNFGU8VYKM65HSN.SEARCH&ssid=z05xatsz5s0000001596626729474",
      "https://flipkart.com/ifb-7-kg-fully-automatic-front-load-in-built-heater-white/p/itmezw2masejjqhr?pid=WMNEZW2MPRCHZAGZ&lid=LSTWMNEZW2MPRCHZAGZD1WUI7&marketplace=FLIPKART&srno=b_1_16&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNEZW2MPRCHZAGZ.SEARCH&ssid=z05xatsz5s0000001596626729474",
      "https://flipkart.com/ifb-6-5-kg-fully-automatic-front-load-in-built-heater-silver/p/itmffu3fwsgzdx2e?pid=WMNFFU3FH4TXHYUV&lid=LSTWMNFFU3FH4TXHYUVTCTKFB&marketplace=FLIPKART&srno=b_1_17&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNFFU3FH4TXHYUV.SEARCH&ssid=z05xatsz5s0000001596626729474",
      "https://flipkart.com/ifb-7-5-kg-fully-automatic-front-load-in-built-heater-white/p/itmezw2mp2qgzvae?pid=WMNEZW2MY3BJWXFH&lid=LSTWMNEZW2MY3BJWXFHRP5QRV&marketplace=FLIPKART&srno=b_1_18&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNEZW2MY3BJWXFH.SEARCH&ssid=z05xatsz5s0000001596626729474",
      "https://flipkart.com/ifb-7-5-kg-fully-automatic-top-load-gold/p/itmecjtgmutkhcz7?pid=WMNECJTGSAGCTGSF&lid=LSTWMNECJTGSAGCTGSFEQVIYM&marketplace=FLIPKART&srno=b_1_19&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNECJTGSAGCTGSF.SEARCH&ssid=z05xatsz5s0000001596626729474",
      "https://flipkart.com/ifb-6-5-kg-water-softener-aqua-energie-fully-automatic-top-load-white/p/itme7n44cdgabtt9?pid=WMNE7N44XHS42GWD&lid=LSTWMNE7N44XHS42GWDRDLNSQ&marketplace=FLIPKART&srno=b_1_20&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNE7N44XHS42GWD.SEARCH&ssid=z05xatsz5s0000001596626729474",
      "https://flipkart.com/ifb-6-5-kg-3d-wash-fully-automatic-front-load-in-built-heater-silver/p/itm7a76e068274aa?pid=WMNDY9RWJH3MZRE3&lid=LSTWMNDY9RWJH3MZRE3ZT89PD&marketplace=FLIPKART&srno=b_1_21&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNDY9RWJH3MZRE3.SEARCH&ssid=z05xatsz5s0000001596626729474",
      "https://flipkart.com/ifb-9-5-kg-fully-automatic-top-load-grey/p/itmejfgg5xyaqkuz?pid=WMNEJFGGZ477AKCQ&lid=LSTWMNEJFGGZ477AKCQGARDZO&marketplace=FLIPKART&srno=b_1_22&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNEJFGGZ477AKCQ.SEARCH&ssid=z05xatsz5s0000001596626729474",
      "https://flipkart.com/ifb-6-5-kg-wifi-enabled-fully-automatic-front-load-in-built-heater-white/p/itmfgu8vsw2zg4nu?pid=WMNFJY5UKSHFCFVR&lid=LSTWMNFJY5UKSHFCFVRUCTPOV&marketplace=FLIPKART&srno=b_1_23&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNFJY5UKSHFCFVR.SEARCH&ssid=z05xatsz5s0000001596626729474",
      "https://flipkart.com/ifb-8-kg-water-softener-aqua-energie-3d-wash-fully-automatic-front-load-in-built-heater-silver/p/itmdy9svcvgva3dh?pid=WMNDY9RWHWHFKFRP&lid=LSTWMNDY9RWHWHFKFRPHXSDXH&marketplace=FLIPKART&srno=b_1_24&otracker=CLP_Filters&fm=organic&iid=3f57b3fa-d5d5-4581-8670-a4d0a1920db4.WMNDY9RWHWHFKFRP.SEARCH&ssid=z05xatsz5s0000001596626729474"
    ]

    def parse(self, response):
        items = Flkt1Item()
        product_name = response.css('._35KyD6::text').extract()
        product_rating = response.css('._1i0wk8').css('::text').extract()
        product_price = response.css('._3qQ9m1').css('::text').extract()
        no_ratings = response.css('._2yc1Qo:nth-child(2) span').css('::text').extract()
        highlights = response.css('.g2dDAR').css('::text').extract()
        prod_desc = response.css('._2THx53').css('::text').extract()
        gen_spec = response.css('._2RngUh').css('::text').extract()
        wash_mod = response.css('._2RngUh:nth-child(4)').css('::text').extract()
        body_feat = response.css('._2RngUh:nth-child(5)').css('::text').extract()
        conv_feat = response.css('._2RngUh:nth-child(6)').css('::text').extract()
        pow_feat = response.css('._2RngUh:nth-child(7)').css('::text').extract()
        add_feat = response.css('._2RngUh:nth-child(8)').css('::text').extract()
        dimensions = response.css('._2RngUh:nth-child(9)').css('::text').extract()

        #cleaning
        prices = [item.strip('\u20b9') for item in product_price]
        ratings = [item.strip(' Ratings &') for item in no_ratings]
        #highlights2 = [item.replace('Highlights, ','') for item in highlights]

        items['product_name'] = product_name
        items['product_rating'] = product_rating
        items['product_price'] = prices
        items['no_ratings'] = ratings
        items['highlights'] = highlights
        items['prod_desc'] = prod_desc
        items['gen_spec'] = gen_spec
        items['wash_mod'] = wash_mod
        items['body_feat'] = body_feat
        items['conv_feat'] = conv_feat
        items['pow_feat'] = pow_feat
        items['add_feat'] = add_feat
        items['dimensions'] = dimensions

        yield items
