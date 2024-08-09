import scrapy
from scrapy.loader import ItemLoader
from jumiascraper.items import JumiascraperItem, JumiaReviewItem

class ProductsSpider(scrapy.Spider):
    
    name = "products"
    # allowed_domains = ["www.jumia.co.ke"]
    start_urls = ["https://www.jumia.co.ke/mlp-garnier-store/"]
    
    
    def start_requests(self):
    
        for page in range(3):
            
            url = f"https://www.jumia.co.ke/mlp-garnier-store/?page={page}#catalog-listing"
            
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self, response):
        
        for product in response.css("article.prd._fb.col.c-prd"):
            
            item = ItemLoader(item=JumiascraperItem(), selector=product)
            
            item.add_css("product", "h3::text")
            item.add_css("price", "div.info div.prc::text")
            item.add_css("store", "div.bdg._mall._xs::text")
            
            product_link = product.css("a.core::attr(href)").get()
            
            url = response.urljoin(product_link)
            
            # url = f"https://www.jumia.co.ke{product_link}"
                
            yield scrapy.Request(url=url, callback=self.parse_description,  meta={"item": item}) # cb_kwargs={"item": item}
                          
                
    def parse_description(self, response): #item
        
        item = response.meta ["item"]
        item.selector = response
         
        item.add_css("brand", "div.-pvxs a:nth-child(1)::text")
        item.add_css("avg_rating", "div.stars._m._al::text")
        item.add_css("number_ratings", "div.-df.-i-ctr.-pbs a.-plxs._more::text")
        item.add_css("number_reviews", "div.cola.-phm.-df.-d-co h2.-fs14.-m.-upp.-ptm::text")
        
        yield item.load_item()
        
        # item.add_css("description", "header.-pvs.-bb")
        # item.add_css("description", "div.markup.-mhm.-pvl.-oxa.-sc p::text")
        
        # paragraphs = response.css("div.markup.-mhm.-pvl.-oxa.-sc p::text").getall()
        
        # if not paragraphs:
        #     text = response.css("div.markup.-mhm.-pvl.-oxa.-sc::text").get()
        #     if text:
        #         paragraphs = [text]
                
        # item.add_value("description", ' '.join(paragraphs))
        
        # item.add_css("rating_five", "ul.-ptxs.-mts.-pbm li:nth-child(1) p::text")
        # item.add_css("rating_four", "ul.-ptxs.-mts.-pbm li:nth-child(2) p::text")
        # item.add_css("rating_three", "ul.-ptxs.-mts.-pbm li:nth-child(3) p::text")
        # item.add_css("rating_two", "ul.-ptxs.-mts.-pbm li:nth-child(4) p::text")
        # item.add_css("rating_one", "ul.-ptxs.-mts.-pbm li:nth-child(5) p::text")
        # item.add_css("number_of_rating", "div.col4.-phm h2::text")
        
        review_link = response.css("header.-df.-i-ctr.-j-bet.-bb.-pvs a::attr(href)").get()
        
        url = response.urljoin(review_link)
        
        yield scrapy.Request(url=url, callback=self.parse_reviews, meta={"product": item.load_item()}) # cb_kwargs={"item": item}
        
        
    def parse_reviews(self, response): #  item
        
        product = response.meta["product"]
         
         
        for review in response.css("article.-pvs.-hr._bet"):
            
            RItem = ItemLoader(item=JumiaReviewItem(), selector=review)
            
            RItem.add_value("product", product["product"])
            RItem.add_css("header", "h3::text")
            RItem.add_css("review", "p::text")
            RItem.add_css("date_reviewed", "div.-df.-j-bet.-i-ctr.-gy5 span.-prs::text")
            
            yield RItem.load_item()
            
            # item.add_css("main_review", "h3::text")
            # item.add_css("additional_review", "p::text")
            # item.add_css("review_date", "div.-df.-j-bet.-i-ctr.-gy5 div.-pvs span:nth-child(1)::text"  
            
        # Pagination
        next_page_link = response.css("div.pg-w.-mhm.-ptl.-pbxl.-bt a:nth-child(6)::attr(href)").get()
        if next_page_link:
            url = response.urljoin(next_page_link)
            yield scrapy.Request(url=url, callback=self.parse_reviews, meta={"product": product}) # , cb_kwargs={"item": item}
            
            
        
        
        
       
        
        
        
        
            
            
        
    
    
    

 
        
