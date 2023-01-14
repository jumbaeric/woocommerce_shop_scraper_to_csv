# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class ProductTypePipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('type'):
            if "product-type-simple" in adapter['type']:
                adapter['type'] = "simple"
            elif "product-type-variable" in adapter['type']:
                adapter['type'] = "variation"
            else:
                adapter['type'] = ""
            return item
        else:
            raise DropItem(f"Missing options in {item}")

class ProductInStockPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('inStock'):
            if "instock" in adapter['inStock']:
                adapter['inStock'] = "1"
            else:
                adapter['inStock'] = "0"
            return item
        else:
            raise DropItem(f"Missing options in {item}")
class DuplicatesPipeline:

    def __init__(self):
        self.names_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['productName'] in self.names_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.names_seen.add(adapter['productName'])
            return item
