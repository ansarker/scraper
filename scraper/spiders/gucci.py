import time
import scrapy
from scrapy.utils.project import get_project_settings
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys

from scraper.gucciItem import GucciItem


class GucciSpider(scrapy.Spider):
    name = 'gucci'
    
    def __init__(self, category=None, url=None, **kwargs):
        super().__init__(**kwargs)
        self.category = category
        self.url = url
        self.headers = {
            'authority': self.url,
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
        }
        self.options = ChromeOptions()
        self.options.headless = False
        
        self.settings = get_project_settings()
        self.driver_path = self.settings.get("CHROME_DRIVER_PATH")
        self.driver = Chrome(executable_path=self.driver_path, options=self.options)
        self.driver.set_page_load_timeout(20)
        self.driver.implicitly_wait(20)
        # self.driver.maximize_window()
        self.driver.set_window_size(1366, 768)
        self.driver.get(self.url)
        
        try:
            buttons = self.driver.find_elements_by_xpath('//div[@class="ajax-loader-link-container ajax-loader-bottom-link-container"]/a')
            if len(buttons) > 0:
                print("load more button exists")
                if buttons[0].is_displayed():
                    buttons[0].click()
                    time.sleep(2)
                else:
                    print("button not displayed")
            else:
                print("no button to load more")
        except:
            print('No page loading...')

    def start_requests(self):
        xpath = '//a[@class="product-tiles-grid-item-link js-ga-track"]'
        links_el = self.driver.find_elements_by_xpath(xpath)
        links = []
        
        for link in links_el:
            links.append(link.get_attribute("href"))
        
        for url in links:
            self.driver.get(url)
            product_name = self.driver.find_elements_by_xpath('//h1[@class="product-name product-detail-product-name"]')
            imgs = self.driver.find_elements_by_xpath('//div[@class="slick-track"]/div/picture/source[@data-image-size="standard-retina"]')
            img_urls = [img.get_property("srcset") for img in imgs]
            yield scrapy.Request(url=url, callback=self.parse_gucci, headers=self.headers, meta={"product_name": product_name[0].text, "img_urls": img_urls}, dont_filter=True)

    def parse_gucci(self, response):
        item = GucciItem()
        item['product_name'] = response.meta["product_name"]
        item['category'] = self.category
        item['url'] = response.url
        item['img_url'] = response.meta["img_urls"]
        print(item)
        return item
