from twisted.internet import reactor
import scrapy

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from jobs.spiders.bulldogjob import BulldogjobSpider


settings = get_project_settings()
configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner(settings)

d = runner.crawl(BulldogjobSpider)
d.addBoth(lambda _: reactor.stop())
reactor.run()