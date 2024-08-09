# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# from doctest import OutputChecker
import scrapy
from itemloaders.processors import  MapCompose, TakeFirst


class JumiascraperItem(scrapy.Item):
    
    product = scrapy.Field(
        input_processor = MapCompose(),
        output_processor = TakeFirst()
    )
    
    price = scrapy.Field(
        input_processor = MapCompose(),
        output_processor = TakeFirst()
    )
    
    store = scrapy.Field(
        input_processor = MapCompose(),
        output_processor = TakeFirst()
    )

    brand = scrapy.Field(
        input_processor = MapCompose(),
        output_processor = TakeFirst()
    )
    
    number_ratings = scrapy.Field(
        input_processor = MapCompose(),
        output_processor = TakeFirst()
    )
    
    avg_rating = scrapy.Field(
        input_processor = MapCompose(),
        output_processor = TakeFirst()
    )
    
    number_reviews = scrapy.Field(
        input_processor = MapCompose(),
        output_processor = TakeFirst()
    )
    

    
class JumiaReviewItem(scrapy.Item):
    
    product = scrapy.Field(
        input_processor = MapCompose(),
        output_processor = TakeFirst()
    )
    
    
    header = scrapy.Field(
        input_processor = MapCompose(),
        output_processor = TakeFirst()
    )
    
    review = scrapy.Field(
        input_processor = MapCompose(),
        output_processor = TakeFirst()
    )
    
    date_reviewed = scrapy.Field(
        input_processor = MapCompose(),
        output_processor = TakeFirst()
    )
    