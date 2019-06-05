import scrapy


class Data(scrapy.Spider):
    name = 'Data'

    start_urls = [
        r'https://data.gov.in/search/site?query=high&field_search=title%5E2&item=100&exact_match=1'
    ]

    def parse(self, response):
        links = response.xpath('//div[@class=\'row\']//h3//a/@href').getall()

        for link in links:
            yield scrapy.Request(
                link,
                callback=self.parse_subpage
            )

    def parse_subpage(self, response):
        # import ipdb; ipdb.set_trace()

        # yield response.xpath('//a[@class=\'json\']/@href').getall()
        
        pass