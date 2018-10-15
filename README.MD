Super simple web scraper for scraping offers that interests me from recruitment sites, and send me the details via mail.
Mainly did this to learn scrapy and fiddle with docker.

To run, remember to set your enviromental variables:
MAIL_USERNAME
MAIL_PASSWORD

to relevant gmail credentials.

If you want to use the docker verion, remember to pass enviromental variables to the container:

```
docker run -e MAIL_USERNAME -e MAIL_PASSWORD <<container id/tag>>
```

Current sites only include bulldogjobs.pl
