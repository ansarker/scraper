import scrapy

from scraper.bookItems import BookItem


class BookSpider(scrapy.Spider):
    name = 'book'
    
    def __init__(self, name=None, category=None, **kwargs):
        super().__init__(name, **kwargs)
        self.category = category
        self.allowed_domains = ['https://parade.com/937586/parade/life-quotes/']
        self.start_urls = [
    "https://www.pdfdrive.com/the-complete-yoga-poses-e33413615.html",
    "https://www.pdfdrive.com/handbook-of-medicinal-herbs-e6646387.html",
    "https://www.pdfdrive.com/teaching-organic-farming-gardening-e17328434.html",
    "https://www.pdfdrive.com/gardens-outdoor-fine-woodworking-e16582922.html",
    "https://www.pdfdrive.com/growing-elite-marijuana-e23769539.html",
    "https://www.pdfdrive.com/plant-biotechnology-and-genetics-principles-techniques-e15853574.html",
    "https://www.pdfdrive.com/vegetable-gardening-for-dummies-e34315490.html",
    "https://www.pdfdrive.com/dubai-abu-dhabi-7-e34802642.html",
    "https://www.pdfdrive.com/india-rajasthan-e33633462.html",
    "https://www.pdfdrive.com/organic-gardening-for-dummies-e33418788.html",
    "https://www.pdfdrive.com/morocco-sleeping-eating-e34358607.html",
    "https://www.pdfdrive.com/japanese-gardens-e28618150.html",
    "https://www.pdfdrive.com/gardening-basics-for-e33672205.html",
    "https://www.pdfdrive.com/fundamentals-organic-farming-gardening-e894453.html",
    "https://www.pdfdrive.com/teaching-organic-farming-and-gardening-center-for-agroecology-e16324851.html",
    "https://www.pdfdrive.com/medicinal-plants-in-folk-tradition-e33432427.html",
    "https://www.pdfdrive.com/handbook-of-plant-and-crop-physiology-e16533919.html",
    "https://www.pdfdrive.com/a-handbook-of-native-american-herbs-e33636932.html",
    "https://www.pdfdrive.com/lonely-planet-guide-e34376908.html",
    "https://www.pdfdrive.com/dictionary-of-flowers-and-plants-for-gardening-e18885013.html",
    "https://www.pdfdrive.com/sri-lanka-13e-2015-e33460646.html",
    "https://www.pdfdrive.com/house-and-leisure-e27033471.html",
    "https://www.pdfdrive.com/permaculture-e34566502.html",
    "https://www.pdfdrive.com/adelaide-south-australia-e33720297.html",
    "https://www.pdfdrive.com/london-for-dummies-6th-edition-e19551265.html",
    "https://www.pdfdrive.com/download-dive-guide-to-the-philippines-e21346612.html",
    "https://www.pdfdrive.com/lonely-planet-japanese-phrasebookpdf-e18901006.html",
    "https://www.pdfdrive.com/ultimate-travelist-e34328327.html",
    "https://www.pdfdrive.com/gardening-for-insects-e14597185.html",
    "https://www.pdfdrive.com/the-rough-guide-to-montenegro-e32299217.html",
    "https://www.pdfdrive.com/greece-peloponnese-e18724100.html",
    "https://www.pdfdrive.com/explore-travel-guides-colombia-e13425786.html",
    "https://www.pdfdrive.com/vegetable-gardening-basics-e27330384.html",
    "https://www.pdfdrive.com/home-gardens-in-nepal-e11854116.html",
    "https://www.pdfdrive.com/a-travellers-guide-to-making-a-difference-around-the-world-e36139206.html",
    "https://www.pdfdrive.com/bangkok-lonely-planet-e18241408.html",
    "https://www.pdfdrive.com/landscape-irrigation-products-e10255427.html",
    "https://www.pdfdrive.com/thailand-e34335797.html",
    "https://www.pdfdrive.com/california-e21896286.html",
    "https://www.pdfdrive.com/lonely-planet-pacific-northwests-best-trips-2e-2013-e34389763.html",
    "https://www.pdfdrive.com/the-sudan-handbook-e29904975.html",
    "https://www.pdfdrive.com/ecuador-gu%C3%ADa-de-oro-p%C3%A1gina-principal-e34131508.html",
    "https://www.pdfdrive.com/africa-13-lonely-planet-e16210891.html",
    "https://www.pdfdrive.com/lonely-planet-new-york-the-mid-atlantics-best-trips-2e-2014-e33532712.html",
    "https://www.pdfdrive.com/the-travel-issue-san-diego-e23162699.html",
    "https://www.pdfdrive.com/choosing-the-right-plants-university-of-nevada-reno-e4623567.html",
    "https://www.pdfdrive.com/chicago-travel-guide-e19858585.html",
    "https://www.pdfdrive.com/malaysia-e34536129.html",
    "https://www.pdfdrive.com/misadventures-in-far-away-places-e21900634.html",
    "https://www.pdfdrive.com/roses-for-canadians-for-dummies-e19519836.html",
    "https://www.pdfdrive.com/understand-survival-lonely-planet-e13754802.html",
    "https://www.pdfdrive.com/strategic-implications-of-chinas-underground-great-wall-e6629122.html",
    "https://www.pdfdrive.com/living-blue-planet-report-e25586788.html",
    "https://www.pdfdrive.com/travels-in-a-tin-can-e635035.html",
    "https://www.pdfdrive.com/the-journal-of-san-diego-history-e22779090.html",
    "https://www.pdfdrive.com/to-travel-here-is-to-encounter-men-wear-e17153762.html",
    "https://www.pdfdrive.com/native-species-planting-guide-for-new-york-city-e19080052.html"
]


    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url)

    def parse(self, response):
        item = BookItem()

        title = response.xpath('//h1[@class="ebook-title ebook-title-bg"]/text()').extract()
        pagecount = response.xpath('//div[@class="ebook-file-info"]/span[1]/text()').extract()
        year = response.xpath('//div[@class="ebook-file-info"]/span[3]/text()').extract()
        img_url = response.xpath('//div[@class="ebook-left"]/a/img[@class="ebook-img"]/@src').extract()

        item['category'] = self.category
        item['title'] = title[0]
        item['pagecount'] = pagecount[0]
        item['year'] = year[0]
        item['img_url'] = img_url[0]
        
        return item
