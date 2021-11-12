# Notes for Scrapy tutorial project
The project is located on a relevant named folder to characterize it. The main object is to scrap data from a rolex auction page.

To invoke Spider go to the folder /watchie/spiders and apply the following command.
```
$ scrapy crawl watches
````

The spider will collect the data with relevant algorithms on /watchie/spiders/watch_spider.py and save it to csv file through pandas.

## Aditional notes for suggested methods on data scraping.

To establish a data-stream or real-time data the most important thing to establish a buffer zone for the pipeline. Since the data stream is in high frequencies like in bitcoin example the data stream will be huge to undertake. So a memory calculation should be made and a processing over data size should be considered.

As extra for changing site types for the establishers the parsing algorithms should be more generalized and applicable for broad ranges. Since the site should have a base structure on display, a generalized system on parsing will give more robustness.