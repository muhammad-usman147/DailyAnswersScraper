# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class PicWordItem(scrapy.Item):

    title = scrapy.Field(
        output_processor = TakeFirst()
    )
    post_date = scrapy.Field(
        output_processor = TakeFirst()
    )
    description = scrapy.Field(
        output_processor = TakeFirst()
    )
    featured_image_url = scrapy.Field(
        output_processor = TakeFirst()
    )
    body_image_url = scrapy.Field(
        output_processor = TakeFirst()
    )
    answer = scrapy.Field(
        output_processor = TakeFirst()
    )
    post_url = scrapy.Field(
        output_processor = TakeFirst()
    )

