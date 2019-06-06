import scrapy

from selenium import webdriver

from os import getcwd, path

from time import sleep

# It is also possible to download the files through the id of the document,
# present in the body tag, and the URL https://data.gov.in/node/id/download


class Data(scrapy.Spider):
    name = 'Data'

    start_urls = [
        r'https://data.gov.in/search/site?query=maharajganj&field_search=title%5E2&item=100&exact_match=1'
    ]

    @classmethod
    def chrome_options(cls):
        options = webdriver.ChromeOptions()

        preferences = {
            'download.default_directory': path.join(getcwd(), 'csv')
        }

        options.add_experimental_option('prefs', preferences)

        return options

    def parse(self, response):
        links = response.xpath('//div[@class=\'row\']//h3//a/@href').getall()
        
        # Get CSV files
        driver = webdriver.Chrome(
            executable_path=path.join(getcwd(), 'chromedriver'),
            chrome_options=Data.chrome_options()
        )

        for link in links:
            driver.get(link)

            sleep(2.5)

            # Click on a CSV
            driver.find_element_by_xpath(
                '//html/body/div[1]/div[1]/div/div[7]/div/div[2]/section/div/div/div/div/div/article/div/div/div[2]/div/div[1]/div/div[2]/div/a'
            ).click()

            # Click on label usage type (non-commercial)
            sleep(1.5)

            driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[7]/div/div[2]/section/div/div/div/div/div/article/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/form/div/div[4]/div/div[2]/label').click()

            # Click on label purpose (academia)
            driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/div[7]/div/div[2]/section/div/div/div/div/div/article/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/form/div/div[5]/div/div[1]'
            ).click()

            # Click on submit
            driver.find_element_by_xpath('//*[@id=\'edit-submit\']').click()
            
            sleep(5)

        driver.close()
        
        # Get XML, JSON, JSONP, XLS or ODS
        # sublinks = response.xpath(
        #     '//a[@class=\'json xml jsonp xls ods\']/@href'
        # ).getall()