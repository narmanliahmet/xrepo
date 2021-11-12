from typing import final
import scrapy
import re
import lxml
import pandas as pd


class QuotesSpider(scrapy.Spider):
    name = "watches"

    def start_requests(self):
        urls = [
            'https://www.christies.com/lot/lot-6338411?ldp_breadcrumb=back&intObjectID=6338411&from=salessummary&lid=1',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        root = lxml.html.fromstring(response.body)

        # optionally remove tags that are not usually rendered in browsers
        # javascript, HTML/HEAD, comments, add the tag names you dont want at the end
        realr = '"price_realised":(\d+)'
        estlowr = '"estimate_low":(\d+)'
        esthighr = '"estimate_high":(\d+)'
        titler = '"title_primary_txt":(.*),"title_secondary_txt"'
        titler2 = '"title_secondary_txt":(.*),"title_tertiary_txt"'
        startr = '"start_date":(.*),"end_date"'
        endr = '"end_date":(.*),"registration_close_date"'
        curr = '"currency_txt":(.*),"closed_txt"'
        locr = '"location_txt":(.*),"url"'
        # complete text
        body = lxml.html.tostring(root, method="text", encoding=lxml.html.unicode)
        real = re.findall(realr, body)
        estlow = re.findall(estlowr, body)
        esthigh = re.findall(esthighr, body)
        title = re.findall(titler, body)
        start = re.findall(startr, body)
        end = re.findall(endr, body)
        cur = re.findall(curr, body)
        title2 = re.findall(titler2, body)
        loc = re.findall(locr, body)
        loc = loc[0]
        loc = loc[1:-1]
        cur = cur[0]
        cur = cur[1:-1]
        end = end[0]
        end = end[1:-8]
        start = start[0]
        start = start[1:-8]
        title = title[0]
        title = title[1:-3]
        title2 = title2[0]
        title2 = title2[1:-3]
        title2 = title2.split(", ")
        brand = title2[0]
        model = title2[1]
        ref = title2[2]
        circ = title2[3]
        data = {'name':title, 'start_date':start, 'end_date':end, 'location':loc, 'brand':brand, 'model':model, 'ref': ref, 'circa': circ
        , 'low_est':estlow, 'high_est':esthigh, 'real':real, 'currency':cur}
        df = pd.DataFrame(data)
        df.to_csv('watch_inspect.csv')