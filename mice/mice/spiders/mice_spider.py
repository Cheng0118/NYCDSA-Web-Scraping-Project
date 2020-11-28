from scrapy import Spider, Request
from mice.items import MiceItem
import re

class MiceSpider(Spider):
	name = 'mice_spider'
	allowed_urls = ['https://www.newegg.com/']
	start_urls = ['https://www.newegg.com/p/pl?N=100160909%204814%201100858365%20600009602']

	def parse(self, response):
		num_pages = int(response.xpath('//span[@class="list-tool-pagination-text"]/strong/text()').extract()[2])

		result_urls = [f'https://www.newegg.com/p/pl?N=100160909%204814%201100858365%20600009602&page={i+1}' for i in range(num_pages)]

		for url in result_urls:
			yield Request(url=url, callback = self.parse_results_page)

	def parse_results_page(self, response):

		product_urls = response.xpath('//div[@class="item-info"]/a/@href').extract()

		for url in product_urls:
			yield Request(url = url, callback = self.parse_product_page)

	def parse_product_page(self, response):

		name = response.xpath('//table[@class="table-horizontal"]//th[text() = "Name"]/following-sibling::td/text()').extract_first()
		brand = response.xpath('//table[@class="table-horizontal"]//th[text() = "Brand"]/following-sibling::td/text()').extract_first()
		model = response.xpath('//table[@class="table-horizontal"]//th[text() = "Model"]/following-sibling::td/text()').extract_first()


		price_all = response.xpath('//li[@class="price-current"]//text()').extract()
		price = float(price_all[1] + price_all[2])



		style = response.xpath('//table[@class="table-horizontal"]//th[text() = "Mouse Grip Style"]/following-sibling::td/text()').extract_first()



		ctype = response.xpath('//table[@class="table-horizontal"]//th[text() = "Type"]/following-sibling::td/text()').extract_first()



		buttons = response.xpath('//table[@class="table-horizontal"]//th[text() = "Buttons"]/following-sibling::td/text()').extract_first()




		dpi = response.xpath('//table[@class="table-horizontal"]//th[text() = "Maximum dpi"]/following-sibling::td/text()').extract_first()


		color = response.xpath('//table[@class="table-horizontal"]//th[text() = "Color"]/following-sibling::td/text()').extract_first()




		# try:
		# 	style = response.xpath('//table[@class="table-horizontal"]//th[text() = "Design Style"]/following-sibling::td/text()').extract_first()
		# except:
		# 	style = 'NA'

		# try:
		# 	mechanical = response.xpath('//table[@class="table-horizontal"]//th[text() = "Mechanical Keyboard"]/following-sibling::td/text()').extract_first()
		# except:
		# 	mechanical = 'NA'

		# try:
		# 	switch = response.xpath('//table[@class="table-horizontal"]//th[text() = "Key Switch Type"]/following-sibling::td/text()').extract_first()
		# except:
		# 	switch = 'NA'

		# try:
		# 	backlit = response.xpath('//table[@class="table-horizontal"]//th[text() = "Backlit"]/following-sibling::td/text()').extract_first()
		# except:
		# 	backlit = 'NA'

		# try:
		# 	color = response.xpath('//table[@class="table-horizontal"]//th[text() = "Keyboard Color"]/following-sibling::td/text()').extract_first()
		# except:
		# 	color = 'NA'

		try:
			reviews = int(response.xpath('//div[@class="product-wrap"]//span[@class="item-rating-num"]/text()').extract()[1])

			rating = int(response.xpath('//div[@class="product-rating"]/i/@class').extract_first()[-1])

		except:
			reviews = 0

			rating = 'NA'


		item = MiceItem()

		item['name'] = name
		item['brand'] = brand
		item['model'] = model
		item['price'] = price
		item['style'] = style
		item['ctype'] = ctype
		item['buttons'] = buttons
		item['dpi'] = dpi
		item['color'] = color
		item['reviews'] = reviews
		item['rating'] = rating


		yield item







