import scrapy
import time
from scrapy.spiders import Spider
from selenium import webdriver
from scrapy import Selector


from scraper_app.items import Player


class PlayerSpider(Spider):
    name = 'PlayerSpider'
    allowed_domains = ["premierleague.com"]
    start_urls = ["https://www.premierleague.com/clubs"]

    def parse(self, response):
        for link in response.xpath('//*[@id="mainContent"]/div[2]/div/div/div[1]/div/ul/li[1]/a/@href'):
            url = response.urljoin(link.extract())
            yield scrapy.Request(url, callback = self.parse_dir_club)

    def parse_dir_club(self, response):
        for link in response.xpath('//*[@id="mainContent"]/nav/ul/li[2]/a/@href'):
            url = response.urljoin(link.extract())
            yield scrapy.Request(url, callback = self.parse_dir_squad)

    def parse_dir_squad(self, response):
        for link in response.xpath('//*[@id="mainContent"]/div[3]/div/ul/li/a/@href'):
            url = response.urljoin(link.extract())
            yield scrapy.Request(url, callback = self.parse_dir_player)

    def parse_dir_player(self, response):
        for link in response.xpath('//*[@id="mainContent"]/div[2]/nav/ul/li[2]/a/@href'):
            url = response.urljoin(link.extract())
            yield scrapy.Request(url, callback = self.parse_dir_contents_stats)


    def parse_dir_contents_stats(self, response):
        print('hello')
        driver = webdriver.Chrome()
        driver.get(response.url)
        time.sleep(15)
        followbutton = driver.find_element_by_xpath('//*[@id="mainContent"]/div[3]/div/div/div/div/div/section/div[2]/div[2][@role="button"]')
        followbutton.click()
        driver.find_element_by_xpath('//*[@id="mainContent"]/div[3]/div/div/div/div/div/section/div[2]/ul/li[2]').click()
        time.sleep(15)
        selection = Selector(text=driver.page_source)
        driver.quit()
        item = Player()
        name = response.xpath('//*[@id="mainContent"]/section/div[1]/div/h1/div/text()').extract()[0]
        team = response.xpath('//*[@id="mainContent"]/div[3]/nav/div/section[1]/div/a/text()').extract()[1]
        item['name'] = name
        item['team'] = team
        for sel in selection.xpath('//*[@id="mainContent"]/div[3]/div/div/div/div/div/ul/li/div/div'):
            try:
                print(sel)
                print(sel.xpath('span/text()'))
                print("sel.xpath printed")
                item_name = sel.xpath('span/text()').extract()[0].replace(" ","").lower()
                item_name = item_name.replace("%","")
                item_name = item_name.replace("/", "")
                print(item_name)
                print(sel.xpath('span/span/text()'))
                print("sel.xpath printed")
                item_data = sel.xpath('span/span/text()').extract()[0].replace(",","")
                print(item_data)
                item[item_name] = item_data
            except:
                pass
        yield item












