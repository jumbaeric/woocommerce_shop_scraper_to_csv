import scrapy
from scrapy.http import Response, Request
from woocommerceWebScraping.items import WoocommercewebscrapingItem
import re


class ProductsSpider(scrapy.Spider):
    name = "productsSpider"

    start_urls = [
        'https://www.examplewooshop.com/shop/',
    ]

    # rules = (
    #     Rule(LinkExtractor(restrict_css="ul.products > li.product > a.woocommerce-LoopProduct-link"),
    #          callback="parse_product", follow=True),
    # )

    def parse(self, response: Response):
        product_urls = response.css(
            "ul.products li.product a.woocommerce-LoopProduct-link::attr(href)"
        ).getall()
        yield from response.follow_all(product_urls, callback=self.parse_product)

        next_page = response.css('ul.page-numbers li a.next::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield response.follow(next_page, callback=self.parse)

    def parse_product(self, response):
        product_item = WoocommercewebscrapingItem()

        product_item["productName"] = response.css(
            "h1.product_title::text").get()
        product_item["salePrice"] = re.findall(
            r'(\d[\d.,]*)\b', response.css('div.summary p.price ins bdi::text').get())
        product_item["regularPrice"] = re.findall(
            r'(\d[\d.,]*)\b', response.css('div.summary p.price del bdi::text').get())
        product_item["categories"] = response.css(
            'div.woocommerce-tabs div.product_meta span.posted_in a::text').get()
        product_item["tags"] = response.css(
            'div.woocommerce-tabs div.product_meta span.tagged_as a::text').get()
        
        product_item["type"] = response.css(
            '.product').xpath("@class").get()
        product_item["published"] = 1
        product_item["inStock"] = response.css(
            '.product').xpath("@class").get()
        # product_item["isFeatured"] = response.css(
        #     '.product').xpath("@class").get()
        # product_item["productId"] = response.css(
        #     '.product').xpath("@class").get()

        product_item["attribute_1_name"] = response.css(
            'table.woocommerce-product-attributes tr:nth-child(1) th.woocommerce-product-attributes-item__label::text').get()
        product_item["attribute_1_value"] = response.css(
            'table.woocommerce-product-attributes tr:nth-child(1) td.woocommerce-product-attributes-item__value a::text').getall()
        product_item["attribute_2_name"] = response.css(
            'table.woocommerce-product-attributes tr:nth-child(2) th.woocommerce-product-attributes-item__label::text').get()
        product_item["attribute_2_value"] = response.css(
            'table.woocommerce-product-attributes tr:nth-child(2) td.woocommerce-product-attributes-item__value a::text').getall()
        product_item["attribute_3_name"] = response.css(
            'table.woocommerce-product-attributes tr:nth-child(3) th.woocommerce-product-attributes-item__label::text').get()
        product_item["attribute_3_value"] = response.css(
            'table.woocommerce-product-attributes tr:nth-child(3) td.woocommerce-product-attributes-item__value a::text').getall()
        product_item["attribute_4_name"] = response.css(
            'table.woocommerce-product-attributes tr:nth-child(4) th.woocommerce-product-attributes-item__label::text').get()
        product_item["attribute_4_value"] = response.css(
            'table.woocommerce-product-attributes tr:nth-child(4) td.woocommerce-product-attributes-item__value a::text').getall()
        product_item["attribute_5_name"] = response.css(
            'table.woocommerce-product-attributes tr:nth-child(5) th.woocommerce-product-attributes-item__label::text').get()
        product_item["attribute_5_value"] = response.css(
            'table.woocommerce-product-attributes tr:nth-child(5) td.woocommerce-product-attributes-item__value a::text').getall()
        product_item["attribute_6_name"] = response.css(
            'table.woocommerce-product-attributes tr:nth-child(6) th.woocommerce-product-attributes-item__label::text').get()
        product_item["attribute_6_value"] = response.css(
            'table.woocommerce-product-attributes tr:nth-child(6) td.woocommerce-product-attributes-item__value a::text').getall()
        product_item["attribute_7_name"] = response.css(
            'table.woocommerce-product-attributes tr:nth-child(7) th.woocommerce-product-attributes-item__label::text').get()
        product_item["attribute_7_value"] = response.css(
            'table.woocommerce-product-attributes tr:nth-child(7) td.woocommerce-product-attributes-item__value a::text').getall()
        product_item["attribute_8_name"] = response.css(
            'table.woocommerce-product-attributes tr:nth-child(8) th.woocommerce-product-attributes-item__label::text').get()
        product_item["attribute_8_value"] = response.css(
            'table.woocommerce-product-attributes tr:nth-child(8) td.woocommerce-product-attributes-item__value a::text').getall()
        product_item["attribute_9_name"] = response.css(
            'table.woocommerce-product-attributes tr:nth-child(9) th.woocommerce-product-attributes-item__label::text').get()
        product_item["attribute_9_value"] = response.css(
            'table.woocommerce-product-attributes tr:nth-child(9) td.woocommerce-product-attributes-item__value a::text').getall()
        product_item["attribute_10_name"] = response.css(
            'table.woocommerce-product-attributes tr:nth-child(10) th.woocommerce-product-attributes-item__label::text').get()
        product_item["attribute_10_value"] = response.css(
            'table.woocommerce-product-attributes tr:nth-child(10) td.woocommerce-product-attributes-item__value a::text').getall()

        product_item["shortDescription"] = response.css(
            "div.woocommerce-product-details__short-description").get()
        product_item["description"] = response.css(
            "div.woocommerce-Tabs-panel--description").get()
        product_item["imagesUrl"] = response.css(
            ".woocommerce-product-gallery__image img::attr(src)").getall()

        # print(product_item)
        yield product_item
