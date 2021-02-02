import scrapy
from scrapy.exceptions import CloseSpider

from scrapy.loader import ItemLoader
from ..items import PermanenttsbItem
from itemloaders.processors import TakeFirst


class PermanenttsbSpider(scrapy.Spider):
	name = 'permanenttsb'
	start_urls = ['https://www.permanenttsb.ie/blog/']
	page = 1

	def parse(self, response):
		post_links = response.xpath('//div[@class="articlebloglist__content"]/a[1]')
		yield from response.follow_all(post_links, self.parse_post)

		self.page += 1
		next_page = f'https://www.permanenttsb.ie/blog/?page={self.page}'

		if not post_links:
			raise CloseSpider('no more pages')

		yield response.follow(next_page, self.parse)

	def parse_post(self, response):
		title = response.xpath('//div[@class="headerblogdetails__title"]/h3/text()').get()
		description = response.xpath('//article[@class="contentblogdetails"]/descendant-or-self::*/text()').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//div[@class="headerblogdetails__date"]/p/text()').get()

		item = ItemLoader(item=PermanenttsbItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
