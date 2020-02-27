import scrapy
class newSpider(scrapy.Spider):
    name = "newSpider"
    start_urls = ['http://172.17.50.43/photography']
    def parse(self,response):
        css_sel = 'img'
        for x in response.css(css_sel):
            xpath_sel = "@src"
            css_sel2 = "::attr(src)"
            yield {
                "IMAGE link": x.xpath(xpath_sel).extract_first()
            }
            nextcss_sel = ".next a ::attr(href)"
            next_page = response.css(nextcss_sel).extract_first()
            if next_page:
                yield scrapy.Request(response.urljoin(next_page), callback=self.parse)