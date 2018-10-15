import scrapy

class BulldogjobSpider(scrapy.Spider):
    name = "bulldogjob"
    start_urls = [
        "https://bulldogjob.pl/companies/jobs/s/city,Pozna%C5%84,Szczecin"
    ]

    def parse(self, response):
        r = response.css("section.search-results")
        next_pages = r.css("li.results-list-item::attr(data-item-url)").extract()
        for href in next_pages:
            yield response.follow(href, self.parse_offer)


    def parse_offer(self, response):
        yield {
            'title': response.css(".offer-header > div:nth-child(1) > h1:nth-child(1)::text").extract(),
            'company': response.xpath("//html/body/div[2]/div[3]/div[2]/div[2]/div[1]/div[1]/div/div[2]/h2/a/text()").extract(),
            'salary': response.css("li.pop-fa:nth-child(2) > span:nth-child(2)::text").extract(),
            'requirements': response.css("div.requirements:nth-child(2) > div:nth-child(4) > ul > li > span:nth-child(1) > span:nth-child(2)::text").extract()
        }