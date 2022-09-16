# python scraping tool to scrape gucci


### TOOLS
* python, scrapy, selenium


### CONDA ENVIRONMENT
```bash
conda create -n scraper python=3.8
conda activate scraper
conda install scrapy==2.4.1 selenium==4.1.0 pandas==1.4.1
```

### USAGE
* `scraper crawl gucci --nolog -a category=<CATEGORY_NAME> -a url=<URL_LINK> -o <OUTPUT_JSON_DIR>`

Here,
```bash
--nolog : not to see verbose/log files
category : a category name
url : url to scrape
-o output json file
```