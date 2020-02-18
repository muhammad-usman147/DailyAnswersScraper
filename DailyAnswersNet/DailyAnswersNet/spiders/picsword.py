import scrapy 
from scrapy.loader import ItemLoader
from ..items import PicWordItem


class PicsWordSpider(scrapy.Spider):
    name = 'picword'  # Spider name

    def start_requests(self):
        '''
            The Spider will send a request from this url and the response will
            be handled by url collection method.
        '''
        yield scrapy.Request(
            url='http://dailyanswers.net/4-pics-1-word-daily',
            callback=self.url_collection
        )

    def url_collection(self, response):
        '''
            Here we are scraping all the links of posts from each page.
            And sending request to the post url where we can get title,
            image, date, description and other.
        '''
        for p_url in response.xpath('//h1[@class="entry-title"]/a'):
            url = p_url.xpath('.//@href').get()
            yield scrapy.Request(
                url=url,   
                callback=self.parse
            )   
        
        # Checking is there are older posts or not ; used for pagination
        older_posts_url = response.xpath('//div[@class="nav-previous"]/a/@href').get()
        if older_posts_url:
            yield scrapy.Request(
                url=older_posts_url,
                callback=self.url_collection
            )

    def parse(self, response):
        '''
            Parsing the response (HTML) and extracting data to item loaders.
        '''
        loader = ItemLoader(item=PicWordItem(), response=response)
        loader.add_xpath('title', '//h1[@class="entry-title"]/text()')
        loader.add_xpath('post_date', '//time[@class="entry-date"]/text()')
        #loader.add_xpath('description', '((//div[@class="0d0ffb8f4a75ad44ed2bbe1d91e88f3a"])[2]/parent::node()/p)[1]')
        loader.add_xpath('featured_image_url', '//div[@class="featured-image"]/img/@src')
        loader.add_xpath('body_image_url', '//p/img/@src')
        loader.add_xpath('answer', '//div[@class="solutions"]/p/strong/text()')
        loader.add_value('post_url', response.url)

        yield loader.load_item()