# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class WoocommercewebscrapingItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # product related items, such as id,name,price
    categories = Field()
    productId = Field()
    productName = Field()
    regularPrice = Field()
    salePrice = Field()
    type = Field()
    sku = Field()
    shortDescription = Field()
    description = Field()
    weight = Field()
    length = Field()
    width = Field()
    height = Field()
    tags = Field()
    imagesUrl = Field()
    attribute_1_name = Field()
    attribute_1_value = Field()
    attribute_2_name = Field()
    attribute_2_value = Field()
    attribute_3_name = Field()
    attribute_3_value = Field()
    attribute_4_name = Field()
    attribute_4_value = Field()
    attribute_5_name = Field()
    attribute_5_value = Field()
    attribute_6_name = Field()
    attribute_6_value = Field()
    attribute_7_name = Field()
    attribute_7_value = Field()
    attribute_8_name = Field()
    attribute_8_value = Field()
    attribute_9_name = Field()
    attribute_9_value = Field()
    attribute_10_name = Field()
    attribute_10_value = Field()
    published = Field()
    isFeatured = Field()
    inStock = Field()
    pass
